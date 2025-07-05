import json

import pyperclip
import requests

API_ENTRYPOINT = 'https://peq.es/api/v1/shorten/'

long_url = pyperclip.paste()
payload = {'target_url': long_url}
response = requests.post(API_ENTRYPOINT, data=json.dumps(payload)).json()
print(response['shorten_url'], end='')
