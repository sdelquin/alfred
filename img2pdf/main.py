from pathlib import Path

import findersel
from PIL import Image

converted_images = 0
for image_path in findersel.get_selected_files():
    image = Image.open(image_path)
    im_output = image.convert('RGB')
    output_path = Path(image_path).with_suffix('.pdf')
    im_output.save(output_path)
    converted_images += 1

print(converted_images, end='')
