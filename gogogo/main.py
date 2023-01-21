import os
import re
import sys
import webbrowser
from csv import DictReader
from pathlib import Path

f = Path(__file__).parent / 'routes.csv'
target = sys.argv[1].strip().lower()

if target == 'e':
    os.system(f'open {f}')
else:
    url = None
    with open(f) as csvfile:
        routes = DictReader(csvfile)
        for route in routes:
            regex = f'^{route["regex"]}$'
            if m := re.match(regex, target):
                url = route['url']
                if len(groups := m.groups()) > 0:
                    for i, item in enumerate(groups, start=1):
                        placeholder = f'${i}'
                        url = url.replace(placeholder, item)
                break
    if url is None:
        print('ERROR', end='')
    else:
        webbrowser.open(url)
