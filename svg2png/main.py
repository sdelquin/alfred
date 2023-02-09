from pathlib import Path

import findersel
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

converted_images = 0
for svg_path in findersel.get_selected_files():
    drawing = svg2rlg(svg_path)
    png_path = Path(svg_path).with_suffix('.png')
    renderPM.drawToFile(drawing, png_path, fmt='PNG')
    converted_images += 1

print(converted_images, end='')
