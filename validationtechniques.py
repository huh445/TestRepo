import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x480")
root.title("Validation Demo")

def validate():
    number = numberInput.get()
    if number:

        if number.isdigit():
            int(number)
            print(f"the number is a digit and {number}")

        else:
            print(f"the number is not a digit, as it is {number}")
    else:
        print("you did not put anything in the entry")

numberInput = tk.Entry(root)
numberInput.pack()

button = tk.Button(root, text="Validate", command=validate)
button.pack()

root.mainloop()