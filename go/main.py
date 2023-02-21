import re
import sys
import unicodedata
from pathlib import Path

from workflow import Workflow

from .utils import create_db_conn

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

db_conn = create_db_conn()
query = 'SELECT * FROM routes WHERE active=1 ORDER BY hits DESC, last_access DESC'
routes = db_conn.execute(query)

for route in routes:
    name = route['name']
    if not query or match(query_parts, name):
        url = route['url']
        icon = route['icon'] or ''
        wf.newline(title=name, autocomplete=name, subtitle=url, arg=url, icon=icon)

wf.send()
