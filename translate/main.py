import sys

from googletrans import Translator

from workflow import Workflow

wf = Workflow()

src_lang, dest_lang = sys.argv[1].strip().split('-')
text = sys.argv[2].strip().lower()

translator = Translator()
translation = translator.translate(text, src=src_lang, dest=dest_lang)

try:
    for candidate in translation.__dict__()['parts'][0]['candidates']:
        title = candidate.lower()
        if title != text:
            wf.newline(title=title)
except TypeError:
    wf.newline(title=translation.text)
wf.send()
