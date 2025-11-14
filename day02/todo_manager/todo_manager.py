
# Day 2: CLI To-Do Manager (JSON Storage)


import json
import argparse
import os

TASK_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(title):
    tasks = load_tasks()
    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet! Add one using --add <task>")
        return
    print("\n📋 Your Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['title']} [{status}]")


def complete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎯 Task {index} marked as complete!")
    else:
        print("⚠️ Invalid task number.")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['title']}")
    else:
        print("⚠️ Invalid task number.")


def main():
    parser = argparse.ArgumentParser(description="Tejas's CLI To-Do Manager")
    parser.add_argument("--add", metavar="task", help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--done", type=int, help="Mark task number as complete")
    parser.add_argument("--delete", type=int, help="Delete task number")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.done:
        complete_task(args.done)
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
