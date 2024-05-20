import tkinter as tk
from tkinter import Listbox

root = tk.Tk()
root.geometry("640x480")

tasks = []

def addTasks():
    task = addTaskEntry.get()
    tasks.append(str(task))
    listTask.insert(tk.END, str(task))

def removeTask():
    task = listTask.curselection()[0]
    listTask.delete(task)

def completeTasks():    
    task = listTask.curselection()[0]
    listTask.itemconfig(task, bg="#90ee90")

addTask = tk.Button(root, text="Add Task", command=addTasks)
addTask.pack()

addTaskEntry = tk.Entry(root)
addTaskEntry.pack()

removeTaskButton = tk.Button(root, text="Remove Task", command=removeTask)
removeTaskButton.pack()

completeTask = tk.Button(root, text="Complete Task", command=completeTasks)
completeTask.pack()

listTask = tk.Listbox(root)
listTask.pack()
listTask.yview_scroll(1, "units")

root.mainloop()