import sys
from pathlib import Path

import findersel
from PyPDF2 import PdfReader, PdfWriter

split_size = int(sys.argv[1])

processed_files = 0
for pdf_path in findersel.get_selected_files():
    with open(pdf_path, 'rb') as input_file:
        file_id = 0
        reader = PdfReader(input_file)
        for i in range(0, len(reader.pages), split_size):
            writer = PdfWriter()
            stem = Path(pdf_path).stem
            pages = reader.pages[i : i + split_size]
            for page in pages:
                writer.add_page(page)
            output_path = Path(pdf_path).with_stem(f'{stem}_{file_id:02d}')
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            file_id += 1
    processed_files += 1

print(processed_files, end='')
