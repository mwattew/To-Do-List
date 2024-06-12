import tkinter as tk
from tkinter import messagebox, simpledialog
from task import Task
from storage import save_tasks, load_tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = load_tasks()
        
        # Create widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.title_label = tk.Label(self.frame, text="To-Do List", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.complete_button = tk.Button(self.frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.save_button = tk.Button(self.frame, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.load_button = tk.Button(self.frame, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(side=tk.LEFT, padx=10)

        self.update_listbox()

    def add_task(self):
        description = simpledialog.askstring("Input", "Enter a task:")
        if description:
            priority = simpledialog.askstring("Input", "Enter priority (Low, Medium, High):", initialvalue="Medium")
            due_date = simpledialog.askstring("Input", "Enter due date (YYYY-MM-DD):")
            task = Task(description, priority, due_date)
            self.tasks.append(task)
            self.update_listbox()

    def remove_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def complete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]].completed = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def save_tasks(self):
        save_tasks(self.tasks)
        messagebox.showinfo("Info", "Tasks saved successfully.")

    def load_tasks(self):
        self.tasks = load_tasks()
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            self.listbox.insert(tk.END, f"{i}. {task}")