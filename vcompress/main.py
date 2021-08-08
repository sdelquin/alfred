import os
from pathlib import Path

import findersel

FFMPEG_PATH = '/opt/homebrew/bin/ffmpeg'
OUTPUT_FORMAT = '.mp4'
OUTPUT_TEMP_PATH = f'/tmp/vcompress{OUTPUT_FORMAT}'

try:
    for file_path in findersel.get_selected_files():
        input_file = Path(file_path)
        output_file_path = input_file.with_suffix(OUTPUT_FORMAT)
        os.system(f'{FFMPEG_PATH} -i "{input_file}" {OUTPUT_TEMP_PATH}')
        os.rename(OUTPUT_TEMP_PATH, output_file_path)
except Exception as err:
    print(f'❌ Something did not work!\n{err}')
else:
    print('✅ Compression done!')
