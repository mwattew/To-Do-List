import json
from task import Task

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        return []