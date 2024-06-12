class Task:
    def __init__(self, description, priority="Medium", due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = " (Completed)" if self.completed else ""
        due = f" (Due: {self.due_date})" if self.due_date else ""
        return f"{self.description} [Priority: {self.priority}]{due}{status}"