import json
from pathlib import Path


class Workflow:
    '''
    Reference: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
    '''

    def __init__(self, icons_path: Path = Path(__file__).absolute().parent):
        self.items = {'items': []}
        self.icons_path = icons_path

    def _fix_icon(self, fields):
        if 'icon' in fields and not isinstance(path := fields['icon'], dict):
            fields['icon'] = {'path': str(self.icons_path / path)}
        return fields

    def newline(self, title, **kwargs):
        fields = {**{'title': title}, **kwargs}
        fields = self._fix_icon(fields)
        self.items['items'].append(fields)

    def to_json(self):
        return json.dumps(self.items)

    def send(self):
        print(self.to_json())

    def __str__(self):
        return self.to_json()
