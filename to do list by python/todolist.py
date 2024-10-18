import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")

tasks = []

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all_tasks():
    global tasks
    tasks = []
    update_task_listbox()

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

add_task_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=5)


clear_all_button = tk.Button(button_frame, text="Clear All", command=clear_all_tasks)
clear_all_button.pack(side=tk.LEFT, padx=5)


root.mainloop()
