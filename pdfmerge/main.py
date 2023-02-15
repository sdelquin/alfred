from pathlib import Path

import findersel
from PyPDF2 import PdfMerger

OUTPUT_PDF_NAME = 'merged.pdf'

merger = PdfMerger()

merged_files = 0
for pdf_path in findersel.get_selected_files(sort=True):
    merger.append(pdf_path)
    merged_files += 1

output_path = Path(pdf_path).with_name(OUTPUT_PDF_NAME)
merger.write(output_path)
merger.close()
print(merged_files, end='')
