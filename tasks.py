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
    if not items:
        print("No tasks yet!")
        return
    for i, task in enumerate(items, 1):
        status = "x" if task["done"] else " "
        print(f"[{status}] {i}. {task['text']}")

def mark_done(idx):
    items = load_items()
    if 1 <= idx <= len(items):
        items[idx - 1]["done"] = True
        save_items(items)
        print(f"Done: {items[idx - 1]['text']}")
    else:
        print(f"Invalid task number: {idx}")

def delete_task(idx):
    items = load_items()
    if 1 <= idx <= len(items):
        removed = items.pop(idx - 1)
        save_items(items)
        print(f"Deleted: {removed['text']}")
    else:
        print(f"Invalid task number: {idx}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_tasks()
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done":
        mark_done(int(sys.argv[2]))
    elif sys.argv[1] == "delete":
        delete_task(int(sys.argv[2]))
    else:
        print(f"Unknown command: {sys.argv[1]}")
