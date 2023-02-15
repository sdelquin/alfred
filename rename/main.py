from pathlib import Path

import findersel

import workflow

wf = workflow.Workflow()
basename = wf.get_var('basename')
padsize = wf.get_var('padsize', cast=int)

processed_files = 0
for i, file_path in enumerate(findersel.get_selected_files(sort=True), start=1):
    f = Path(file_path)
    new_stem = f'{basename}{i:0{padsize}d}'
    f.rename(f.with_stem(new_stem))
    processed_files += 1

print(processed_files, end='')
