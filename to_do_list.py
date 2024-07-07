import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        tasks.append({"title": task, "completed": False})
        update_task_listbox()
        entry_task.delete(0, tk.END)  # Clear the entry textbox
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
        
def complete_task():
    if task_listbox.curselection():
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]['completed'] = True
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "You must select a task.")
        
def delete_task():
    if task_listbox.curselection():
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    index = 1
    for task in tasks:
        status = "Done" if task['completed'] else "Not Done"
        task_text = f"{index}. {task['title']} - {status}"
        task_listbox.insert(tk.END, task_text)
        if task['completed']:
            task_listbox.itemconfig(tk.END, {'fg': 'grey'})
        else:
            task_listbox.itemconfig(tk.END, {'fg': 'black'})
        index += 1
        
root = tk.Tk()
root.title("Simple To-Do List")

tasks = []
button_width = 20 

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", bg="lightgreen", width=button_width, command=add_task)
button_add_task.pack(pady=5)

button_complete_task = tk.Button(root, text="Complete Task", bg="lightblue", width=button_width, command=complete_task)
button_complete_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", bg="lightcoral", width=button_width, command=delete_task)
button_delete_task.pack(pady=5)

root.mainloop()
