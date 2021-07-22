import sys
from functools import partial
from pathlib import Path

import findersel
from prettyconf import config
from pylovepdf.ilovepdf import ILovePdf

from ilovepdf.services import HiddenPrints

ILOVEPDF_PUBLIC_KEY = config('ILOVEPDF_PUBLIC_KEY')
TRASH_PATH = Path(__file__).home() / '.Trash'

SINGLE_FILE_TOOLS = [
    'compress',
    'imagepdf',  # Not working: https://github.com/AndyCyberSec/pylovepdf/issues/17
    'officepdf',  # Not working: https://github.com/AndyCyberSec/pylovepdf/issues/17
    'pagenumber',
    'pdfa',  # Not working: https://github.com/AndyCyberSec/pylovepdf/issues/17
    'pdfjpg',  # Not working: https://github.com/AndyCyberSec/pylovepdf/issues/17
    'unlock',
]

# https://developer.ilovepdf.com/docs/api-reference
# https://github.com/AndyCyberSec/pylovepdf/tree/master/pylovepdf/samples
ilovepdf = ILovePdf(ILOVEPDF_PUBLIC_KEY, verify_ssl=True)


def single_file_tool(tool: str, *args):
    for file_path in findersel.get_selected_files():
        file = Path(file_path)

        task = ilovepdf.new_task(tool)
        task.add_file(file)
        task.set_output_folder(file.absolute().parent)
        task.execute()
        output_filename = task.download()
        task.delete_current_task()

        output_file = Path(file.with_name(output_filename))
        file.replace(TRASH_PATH / file.name)
        output_file.replace(output_file.with_stem(file.stem))


def merge(*args):
    task = ilovepdf.new_task('merge')
    for file_path in findersel.get_selected_files():
        file = Path(file_path)
        task.add_file(file)

    task.set_output_folder(file.absolute().parent)
    task.execute()
    task.download()
    task.delete_current_task()


def split(*args):
    split_mode, ranges = args
    task = ilovepdf.new_task('split')
    # this operation must be performed over one file
    file = Path(list(findersel.get_selected_files())[0])
    task.add_file(file)
    task.split_mode = split_mode
    setattr(task, split_mode, ranges)
    task.set_output_folder(file.absolute().parent)
    task.execute()
    task.download()
    task.delete_current_task()


for tool in SINGLE_FILE_TOOLS:
    globals()[tool] = partial(single_file_tool, tool)


try:
    # First param should be the name of a tool (functions below)
    tool = sys.argv[1]
    # Rest might be optional params for tools
    args = sys.argv[2:]
    with HiddenPrints():
        globals().get(sys.argv[1])(*args)
except Exception:
    print('❌ Something did not work!')
else:
    print(f'✅ {tool.title()} done!')
