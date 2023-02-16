from pathlib import Path

import findersel

import workflow

wf = workflow.Workflow()
files = list(findersel.get_selected_files(sort=True))
basename = wf.get_arg(1)
padsize = len(str(len(files)))

for i, file_path in enumerate(files, start=1):
    f = Path(file_path)
    new_stem = f'{basename}{i:0{padsize}d}'
    f.rename(f.with_stem(new_stem))

print(len(files), end='')
