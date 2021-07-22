import os
import sys

from prettyconf import config
from pylovepdf import ILovePdf

PUBLIC_KEY = config('ILOVEPDF_PUBLIC_KEY')

# tool names as described in https://github.com/AndyCyberSec/pylovepdf#tools
TOOLS = [
    'compress',
    'imagepdf',
    'merge',
    'officepdf',
    'pagenumber',
    'pdfa',
    'pdfjpg',
    'protect',
    'rotate',
    'split',
    'unlock',
    'validatepdfa',
    'watermark',
]

ilovepdf = ILovePdf(PUBLIC_KEY, verify_ssl=True)

for tool in TOOLS:
    sys.stdout = open(os.devnull, 'w')
    try:
        task = ilovepdf.new_task(tool)
        task.debug = False
        task.delete_current_task()
    except Exception as err:
        sys.stdout = sys.__stdout__
        print(f'TOOL: {tool}')
        print(err)
