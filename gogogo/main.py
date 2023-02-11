import re
import sys
import unicodedata
from csv import DictReader
from pathlib import Path

from workflow import Workflow

BOUNDARY_SYMBOLS = r'[- ():]+'


def match(query_parts, name):
    name_parts = re.split(BOUNDARY_SYMBOLS, name.lower())
    for qpart in query_parts:
        if not any(npart.startswith(qpart) for npart in name_parts):
            return False
    return True


# https://bit.ly/3wBRr4e
query = unicodedata.normalize('NFC', sys.argv[1]).strip().lower()
query_parts = re.split(BOUNDARY_SYMBOLS, query)

wf = Workflow(icons_path=Path(__file__).parent / 'img')
f = Path(__file__).parent / 'routes.csv'

with open(f) as csvfile:
    routes = DictReader(csvfile)
    for route in routes:
        name = route['name']
        if not query or match(query_parts, name):
            url = route['url']
            icon = route.get('icon', '')
            wf.newline(title=name, autocomplete=name, subtitle=url, arg=url, icon=icon)

wf.send()
