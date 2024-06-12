import tkinter as tk
from todo_app import ToDoApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.geometry("500x400")
    root.mainloop()