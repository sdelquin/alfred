import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

from workflow import Workflow

BOUNDARY_SYMBOLS = r'[- ():]+'
CWD = Path(__file__).parent


def match(query_parts, name):
    name_parts = re.split(BOUNDARY_SYMBOLS, name.lower())
    for qpart in query_parts:
        if not any(npart.startswith(qpart) for npart in name_parts):
            return False
    return True


# https://bit.ly/3wBRr4e
query = unicodedata.normalize('NFC', sys.argv[1]).strip().lower()
query_parts = re.split(BOUNDARY_SYMBOLS, query)

wf = Workflow(icons_path=CWD / 'img')
db_path = CWD / 'go.sqlite'

con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row
routes = con.execute('SELECT * FROM routes')

for route in routes:
    name = route['name']
    if not query or match(query_parts, name):
        url = route['url']
        icon = route['icon'] or ''
        wf.newline(title=name, autocomplete=name, subtitle=url, arg=url, icon=icon)

wf.send()
