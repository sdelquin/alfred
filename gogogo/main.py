import sys
import unicodedata
from csv import DictReader
from pathlib import Path

from workflow import Workflow

# https://bit.ly/3wBRr4e
target = unicodedata.normalize('NFC', sys.argv[1])
target = target.strip().lower()

wf = Workflow(icons_path=Path(__file__).parent / 'img')
f = Path(__file__).parent / 'routes.csv'

with open(f) as csvfile:
    routes = DictReader(csvfile)
    for route in routes:
        alias = route['alias']
        description = route['description']
        fixed_target = target.lower().replace(' ', '')
        fixed_alias = alias.lower().replace(' ', '')
        if (
            not target
            or alias.startswith(target)
            or fixed_alias.startswith(fixed_target)
            or target in alias
            or target in description.lower()
        ):
            url = route['url']
            icon = f'{alias.split()[0]}.png'
            wf.newline(
                title=alias, autocomplete=alias, subtitle=description, arg=url, icon=icon
            )

wf.send()
