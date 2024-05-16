import socket

from prettyconf import config

INTERNAL_NETWORK = config('INTERNAL_NETWORK')
MARTE_EXTERNAL_URL = config('MARTE_EXTERNAL_URL', default='marte')
MARTE_INTERNAL_URL = config('MARTE_INTERNAL_URL', default='marte')


def getip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]


if getip().startswith(INTERNAL_NETWORK):
    print(MARTE_INTERNAL_URL)
else:
    print(MARTE_EXTERNAL_URL)
