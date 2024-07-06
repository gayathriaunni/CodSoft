import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        total_time = int(time_entry.get())
        if total_time < 0:
            raise ValueError("Negative value")
        update_timer(total_time)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter positive integer")

def update_timer(total_time):
    if total_time > 0:
        mins, secs = divmod(total_time, 60)
        time_formatted = f'{mins:02d}:{secs:02d}'
        timer_label.config(text=time_formatted)
        root.after(1000, update_timer, total_time - 1)
    else:
        timer_label.config(text="00:00")
        messagebox.showinfo("Time's up", "The countdown has finished!")

root = tk.Tk()
root.title("Countdown Timer")

time_label = tk.Label(root, text="Enter time in seconds:", font=("Helvetica", 12))
time_label.pack()

time_entry = tk.Entry(root, width=20)
time_entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

timer_label = tk.Label(root, text="", font=("Helvetica", 48))
timer_label.pack()

root.mainloop()

