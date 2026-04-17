import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).parent / "items.json"

def load_items():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []

def save_items(items):
    DATA_FILE.write_text(json.dumps(items, indent=2))

def add_task(text):
    items = load_items()
    items.append({"text": text, "done": False})
    save_items(items)
    print(f"Added: {text}")

def list_tasks():
    items = load_items()
    for i, task in enumerate(items, 1):
        status = "x" if task["done"] else " "
        print(f"[{status}] {i}. {task['text']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_tasks()
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
