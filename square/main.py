import findersel
from PIL import Image

SOURCE_BACKGROUND_COLOR_POSITION = (20, 20)


def get_pixel_color(image: Image, x: int, y: int) -> str:
    rgb_image = image.convert('RGB')
    r, g, b = rgb_image.getpixel((1, 1))
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def expand2square(pil_img: Image, background_color: str) -> Image:
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


converted_images = 0
for image_path in findersel.get_selected_files():
    image = Image.open(image_path)
    background_color = get_pixel_color(image, *SOURCE_BACKGROUND_COLOR_POSITION)
    squared_image = expand2square(image, background_color)
    squared_image.save(image_path)
    converted_images += 1

print(converted_images, end='')
