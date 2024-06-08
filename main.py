import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        
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

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter a task:")
        if task:
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
            task = self.tasks[selected_task_index[0]]
            self.tasks[selected_task_index[0]] = f"{task} (Completed)"
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.geometry("400x400")
    root.mainloop()
