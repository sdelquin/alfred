'''
References:
https://dev.bitly.com/
https://dev.bitly.com/api-reference#createBitlink
'''
import json

import pyperclip
import requests
from prettyconf import config

API_ENTRYPOINT = 'https://api-ssl.bitly.com/v4/shorten'

TOKEN = config('BITLY_TOKEN')
GROUP_GUID = config('BITLY_GROUP')
long_url = pyperclip.paste()

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
}

payload = {'long_url': long_url, 'domain': "bit.ly", 'group_guid': GROUP_GUID}

response = requests.post(API_ENTRYPOINT, headers=headers, data=json.dumps(payload))
rfields = response.json()

print(rfields['link'])
