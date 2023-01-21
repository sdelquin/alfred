import re
import sys
import webbrowser
from csv import DictReader
from pathlib import Path

f = Path(__file__).parent / 'routes.csv'
target = sys.argv[1].strip().lower()
with open(f) as csvfile:
    routes = DictReader(csvfile)
    for route in routes:
        regex = f'^{route["regex"]}$'
        url = route['url']
        if m := re.match(regex, target):
            if len(groups := m.groups()) > 0:
                for i, item in enumerate(groups, start=1):
                    placeholder = f'${i}'
                    url = url.replace(placeholder, item)
            break

webbrowser.open(url)
