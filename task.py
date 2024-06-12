class Task:
    def __init__(self, description, priority="Medium", due_date=None, added_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.added_date = added_date
        self.completed = False

    def __str__(self):
        status = " (Completed)" if self.completed else ""
        due = f" (Due: {self.due_date})" if self.due_date else ""
        added = f" (Added: {self.added_date})"
        return f"{self.description} [Priority: {self.priority}]{due}{added}{status}"
