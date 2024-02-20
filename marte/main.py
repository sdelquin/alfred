import socket

from prettyconf import config

HOME_HOSTNAME = config('HOME_HOSTNAME', default='home')
MARTE_EXTERNAL_URL = config('MARTE_EXTERNAL_URL', default='marte')
MARTE_INTERNAL_URL = config('MARTE_INTERNAL_URL', default='marte')

if socket.gethostname().startswith(HOME_HOSTNAME):
    print(MARTE_EXTERNAL_URL)
else:
    print(MARTE_INTERNAL_URL)
