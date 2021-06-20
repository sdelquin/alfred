from pathlib import Path

import findersel
import requests
from prettyconf import config

PHOTOROOM_API_ENTRYPOINT = config(
    'PHOTOROOM_API_ENTRYPOINT', default='https://sdk.photoroom.com/v1/segment'
)
PHOTOROOM_APIKEY = config('PHOTOROOM_APIKEY')


def make_alpha(image_path: str):
    '''image_path: absolute path to the image to be processed'''
    input_image = Path(image_path)
    response = requests.post(
        PHOTOROOM_API_ENTRYPOINT,
        headers={'x-api-key': PHOTOROOM_APIKEY},
        files={'image_file': open(input_image, 'rb')},
    )
    response.raise_for_status()
    output_image = input_image.with_name(input_image.stem + '.png')
    with open(output_image, 'wb') as f:
        f.write(response.content)


num_processed_images = 0
for image_path in findersel.get_selected_files():
    make_alpha(image_path)
    num_processed_images += 1

print(num_processed_images, end='')
