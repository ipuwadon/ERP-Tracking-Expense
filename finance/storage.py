import json
from pathlib import Path


class Storage:
    def __init__(self, file_path):
        self.file = Path(file_path)
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if self.file.exists():
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)

        return {"accounts": {}, "expenses": []}

    def save(self, data):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            