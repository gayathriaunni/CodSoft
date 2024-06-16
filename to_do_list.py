import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks.append({"title": task, "completed": False})
        update_task()
        entry.delete(0, tk.END)  # Clear the entry textbox
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def complete_task():
    if tasklist.curselection():
        selecttask = tasklist.curselection()[0]
        tasks[selecttask]['completed'] = True
        update_task()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

def delete_task():
    if tasklist.curselection():
        selecttask = tasklist.curselection()[0]
        tasks.pop(selecttask)
        update_task()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

def update_task():
    tasklist.delete(0, tk.END)
    index = 1
    for task in tasks:
        status = "Done" if task['completed'] else "Not Done"
        task_text = f"{index}. {task['title']} - {status}"
        tasklist.insert(tk.END, task_text)
        if task['completed']:
            tasklist.itemconfig(tk.END, {'fg': 'grey'})
        else:
            tasklist.itemconfig(tk.END, {'fg': 'black'})
        index += 1
        
root = tk.Tk()
root.title("To-Do List")

tasks = []
bwidth = 20 
tasklist = tk.Listbox(root, width=50, height=10)
tasklist.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)
addbutton = tk.Button(root, text="Add Task", bg="lightgreen", width=bwidth, command=add_task)
addbutton.pack(pady=5)
compbutton = tk.Button(root, text="Complete Task", bg="lightblue", width=bwidth, command=complete_task)
compbutton.pack(pady=5)
delbutton = tk.Button(root, text="Delete Task", bg="lightpink", width=bwidth, command=delete_task)
delbutton.pack(pady=5)

root.mainloop()


