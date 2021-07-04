import sys
from pathlib import Path

import pyperclip
from workflow import Workflow

IVA_FACTOR = 0.82644865925  # based on experience
IGIC = 7
DUA = 13.48
DUA_THRESHOLD = 150


def display(prices: dict):
    def slugify(label):
        return label.lower().replace(' ', '-')

    wf = Workflow(icons_path=Path(__file__).absolute().parent / 'img')
    for label, amount in prices.items():
        icon = f'{slugify(label)}.png'
        wf.newline(title=f'{amount:.2f}€', subtitle=label, arg=amount, icon=icon)
    wf.send()


def calculate_prices(amazon_price: float):
    norm_igic = IGIC / 100

    price_without_iva = amazon_price * IVA_FACTOR
    if price_without_iva < DUA_THRESHOLD:
        full_duty = 0
    else:
        duty_igic = price_without_iva * norm_igic
        full_dua = DUA + DUA * norm_igic
        full_duty = full_dua + duty_igic

    final_price = price_without_iva + full_duty

    return {
        'Final price': final_price,
        'Price without IVA': price_without_iva,
        'Duty': full_duty,
        'Amazon price': amazon_price,
    }


def get_input_price():
    def clean_price(p: str):
        try:
            return float(p.lstrip().rstrip(' €').replace(',', '.'))
        except ValueError:
            return None

    if sys.argv[1]:
        return clean_price(sys.argv[1])
    elif value := clean_price(pyperclip.paste()):
        return value
    else:
        return None


if __name__ == '__main__':
    if input_price := get_input_price():
        prices = calculate_prices(input_price)
        display(prices)
