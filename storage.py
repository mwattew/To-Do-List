import json
from task import Task
from datetime import datetime

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump([task.__dict__ for task in tasks], file, default=str)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            tasks = []
            for data in tasks_data:
                data['due_date'] = datetime.strptime(data['due_date'], "%Y-%m-%d %H:%M") if data['due_date'] else None
                data['added_date'] = datetime.strptime(data['added_date'], "%Y-%m-%d %H:%M") if data['added_date'] else None
                tasks.append(Task(**data))
            return tasks
    except FileNotFoundError:
        return []