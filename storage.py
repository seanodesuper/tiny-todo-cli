"""
Storage utilities for task persistence.
"""
import json
from pathlib import Path
from datetime import datetime

DEFAULT_FILE = Path(__file__).parent / "items.json"

class TaskStorage:
    def __init__(self, filepath=None):
        self.filepath = Path(filepath) if filepath else DEFAULT_FILE

    def load(self):
        if self.filepath.exists():
            try:
                return json.loads(self.filepath.read_text())
            except json.JSONDecodeError:
                return []
        return []

    def save(self, items):
        self.filepath.write_text(json.dumps(items, indent=2))

    def add(self, text, priority="normal"):
        items = self.load()
        task = {
            "text": text,
            "done": False,
            "priority": priority,
            "created": datetime.now().isoformat(),
        }
        items.append(task)
        self.save(items)
        return task

    def get_all(self):
        return self.load()

    def mark_done(self, idx):
        items = self.load()
        if 1 <= idx <= len(items):
            items[idx - 1]["done"] = True
            items[idx - 1]["completed"] = datetime.now().isoformat()
            self.save(items)
            return items[idx - 1]
        return None

    def delete(self, idx):
        items = self.load()
        if 1 <= idx <= len(items):
            removed = items.pop(idx - 1)
            self.save(items)
            return removed
        return None

    def clear_done(self):
        items = self.load()
        remaining = [t for t in items if not t["done"]]
        removed_count = len(items) - len(remaining)
        self.save(remaining)
        return removed_count
