import os
import sys


class HiddenPrints:
    ''' https://stackoverflow.com/a/45669280 '''

    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def fix_rotation_degrees(degrees: int):
    degrees = 360 + degrees if degrees < 0 else degrees
    if 0 <= degrees < 45:
        return 0
    if 45 <= degrees < 90:
        return 90
    if 90 <= degrees < 135:
        return 90
    if 135 <= degrees < 180:
        return 180
    if 180 <= degrees < 225:
        return 180
    if 225 <= degrees < 270:
        return 270
    if 270 <= degrees < 315:
        return 270
    if 315 <= degrees < 360:
        return 0
