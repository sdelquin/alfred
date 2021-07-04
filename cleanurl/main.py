import re

import pyperclip

dirty_url = pyperclip.paste()
cleaned_url = re.sub(r'\?.*', '', dirty_url)
print(cleaned_url, end='')
