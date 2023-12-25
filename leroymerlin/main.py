import shlex
import subprocess

from workflow import Workflow

from .config import PRODUCTS

wf = Workflow()

step = wf.get_var('step', cast=int)
product_name = wf.get_var('product')
size = wf.get_var('size')
product_cfg = PRODUCTS[product_name]

match step:
    case 1:
        for size in sorted(product_cfg['sizes']):
            wf.newline(f'{product_cfg["size_symbol"]} {size} mm', arg=size)
        wf.send()
    case 2:
        url = product_cfg['url'].format(size=size)
        cmd = f'open {url}'
        subprocess.run(shlex.split(cmd))
