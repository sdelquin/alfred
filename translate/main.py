import sys
from pathlib import Path

from workflow import Workflow
from wrpy import WordReference

wf = Workflow(icons_path=Path(__file__).absolute().parent / 'img')

dict_code = sys.argv[1].strip()
text = sys.argv[2].strip().lower()

wr = WordReference(dict_code)
response = wr.translate(text)

for section in response['translations']:
    wf.newline(section['title'], icon='header.png')
    for entry in section['entries']:
        source = entry['from_word']['source']
        meanings = ' • '.join(m['meaning'] for m in entry['to_word'])
        title = f'{source} → {meanings}'
        context = entry.get('context', '')
        if example := entry['to_example'][0] if entry['to_example'] else '':
            subtitle = f'{context} | {example}'
        else:
            subtitle = context
        arg = entry['to_word'][0]['meaning']
        wf.newline(title=title, subtitle=subtitle, arg=arg)

wf.send()
