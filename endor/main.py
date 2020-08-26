from pathlib import Path

import prettyconf
import requests

from workflow import Workflow

API_URL = prettyconf.config('API_URL')

wf = Workflow(icons_path=Path(__file__).absolute().parent / 'img')

r = requests.get(API_URL)
stats = r.json()

current = stats['cpu_freq']['current']
units = stats['cpu_freq']['units']
title = f"{current:.2f}{units}"
subtitle = 'CPU Freq'
icon = 'cpu.png'
wf.newline(title=title, subtitle=subtitle, icon=icon, arg=current)

current = stats['mem_usage']['current']
units = stats['mem_usage']['units']
max_value = stats['mem_usage']['max']
title = f"{current:.2f}{units} / {max_value:.2f}{units}"
subtitle = 'Mem Usage'
icon = 'ram.png'
wf.newline(title=title, subtitle=subtitle, icon=icon, arg=current)

current = stats['disk_usage']['current']
units = stats['disk_usage']['units']
max_value = stats['disk_usage']['max']
title = f"{current:.2f}{units} / {max_value:.2f}{units}"
subtitle = 'Disk Usage'
icon = 'disk.png'
wf.newline(title=title, subtitle=subtitle, icon=icon, arg=current)

current = stats['cpu_load']['current']
units = stats['cpu_load']['units']
title = f"{current:.2f}{units}"
subtitle = 'CPU Load'
icon = 'load.png'
wf.newline(title=title, subtitle=subtitle, icon=icon, arg=current)

wf.send()
