import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("640x480")

def check():
     userFullName = inputFullName.get()
     userAge = int(inputFullName.get())

inputFullName = tk.Entry(root)
inputFullName.pack()

inputAge = tk.Entry(root)
inputAge.pack()

checkButton = tk.Button(root, text="check", command=check)