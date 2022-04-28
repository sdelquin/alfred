# https://es.wikipedia.org/wiki/Impuesto_General_Indirecto_Canario

import sys
from pathlib import Path

from workflow import Workflow

wf = Workflow(icons_path=Path(__file__).absolute().parent / 'img')

iva_price = float(sys.argv[1].strip().lower())
igic_price = iva_price / 1.21 * 1.07

wf.newline(title=f'{igic_price:.2f}€', subtitle='Price with IGIC', arg=igic_price)
wf.send()
