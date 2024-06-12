import tkinter as tk
from tkinter import simpledialog

class TimePickerDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Select Time")
        tk.Label(master, text="Hour:").grid(row=0)
        tk.Label(master, text="Minute:").grid(row=1)

        self.hour = tk.Spinbox(master, from_=0, to=23, width=5)
        self.minute = tk.Spinbox(master, from_=0, to=59, width=5)

        self.hour.grid(row=0, column=1)
        self.minute.grid(row=1, column=1)
        
        return self.hour  # initial focus

    def apply(self):
        self.result = f"{int(self.hour.get()):02}:{int(self.minute.get()):02}"
