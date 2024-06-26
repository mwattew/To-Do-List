import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import Calendar
from task import Task
from storage import save_tasks, load_tasks
from time_picker import TimePickerDialog  # Import the custom time picker
from datetime import datetime

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
            due_date = self.ask_due_date()
            if due_date:
                due_time = self.ask_due_time()
                if due_time:
                    try:
                        print(f"Combining due_date: {due_date} and due_time: {due_time}")  # Debug print
                        combined_due_date = f"{due_date} {due_time}"
                        print(f"Combined due date and time: {combined_due_date}")  # Debug print
                        due_date = datetime.strptime(combined_due_date, "%m/%d/%y %H:%M")
                        print(f"Parsed datetime object: {due_date}")  # Debug print
                    except ValueError as e:
                        print(f"Error parsing date/time: {e}")  # Debug print
                        messagebox.showerror("Error", "Invalid date/time format. Please use the format YYYY-MM-DD and HH:MM.")
                        return
                    added_date = datetime.now().strftime("%Y-%m-%d %H:%M")
                    task = Task(description, priority, due_date, added_date)
                    self.tasks.append(task)
                    self.update_listbox()

    def ask_due_date(self):
        top = tk.Toplevel(self.root)
        top.grab_set()
        cal = Calendar(top, selectmode='day')
        cal.pack(pady=20)
        date_str = tk.StringVar()

        def on_date_select():
            date_str.set(cal.get_date())
            top.destroy()

        select_button = tk.Button(top, text="Select Date", command=on_date_select)
        select_button.pack(pady=20)
        self.root.wait_window(top)
        return date_str.get()

    def ask_due_time(self):
        time_picker = TimePickerDialog(self.root)
        return time_picker.result

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
            status_icon = "✅" if task.completed else "❌"
            self.listbox.insert(tk.END, f"{i}. {status_icon} {task}")
