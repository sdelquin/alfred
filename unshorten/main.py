import re
import shlex
import subprocess

import pyperclip

shortened_url = pyperclip.paste()
cmd = f'curl -ksLI {shortened_url}'
output = subprocess.run(shlex.split(cmd), capture_output=True, encoding='utf-8')
unshortened_url = re.search(r'[Ll]ocation: (.*)', output.stdout).groups()[0]
print(unshortened_url, end='')
