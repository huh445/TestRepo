import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry("640x480")
root.title("Day Selector")

def checkDay():
    day = days.get()
    if day == "Monday":
        print(f"Its {day}! Time to start the week!")
    elif day == "Tuesday":
        print(f"Its {day}! Getting through the week!")
    elif day == "Wednesday":
        print(f"Its {day}! More than halfway!")
    elif day == "Thursday":
        print(f"Its {day}! Almost to the weekend!")
    elif day == "Friday":
        print(f"Its {day}! Not long left NOW!")
    else:
        print(f"weekend, its {day}")
    
days = tk.StringVar(root)
days.set("Select the current DAY!")
dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

dayGet = tk.OptionMenu(root, days, *dayList)
dayGet.pack()

button = tk.Button(root, text="Check", command=checkDay)
button.pack()

root.mainloop()