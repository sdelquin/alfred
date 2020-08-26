import socket
import uuid
from pathlib import Path

import prettyconf
import requests

from workflow import Workflow

IP_SERVICE = prettyconf.config('IP_SERVICE')

wf = Workflow(icons_path=Path(__file__).absolute().parent / 'img')

# Local IP
local_ip = socket.gethostbyname(socket.gethostname())
wf.newline(title=local_ip, subtitle='Local IP', icon='lan.png')

# Public IP
public_ip = requests.get(IP_SERVICE).text
wf.newline(title=public_ip, subtitle='Public IP', icon='router.png')

# MAC address
mac = ':'.join(("%012X" % uuid.getnode())[i : i + 2] for i in range(0, 12, 2))
wf.newline(title=mac, subtitle='MAC', icon='network-card.png')

wf.send()
