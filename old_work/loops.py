import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("640x480")
root.title("Sum Calculator")

def calculateSum():
    if input.get():
        number = input.get()
        if number.isdigit():
            number = int(number)
            i = 0
            total = 0
            while i < number:
                i += 1
                total += i
            print(total)
        else:
            print(f"the input is not a number, but in fact{number}")
    else:
        print("you didnt put anything in the entry")


input = tk.Entry(root)
input.pack()

button = tk.Button(root, text="Calculate", command=calculateSum)
button.pack()

root.mainloop()