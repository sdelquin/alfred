import sys
from csv import DictReader
from pathlib import Path

from workflow import Workflow

wf = Workflow(icons_path=Path(__file__).parent / 'img')
f = Path(__file__).parent / 'routes.csv'
target = sys.argv[1].strip().lower()

with open(f) as csvfile:
    routes = DictReader(csvfile)
    for route in routes:
        alias = route["alias"]
        if not target or alias.startswith(target):
            url = route['url']
            description = route['description']
            icon = f'{alias.split()[0]}.png'
            wf.newline(
                title=alias, autocomplete=alias, subtitle=description, arg=url, icon=icon
            )

wf.send()
