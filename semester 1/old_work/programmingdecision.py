import tkinter as tk

root = tk.Tk()
root.geometry("600x480")

def checkAge():
    age1 = ageEntry.get()
    if age1:
        age = int(age1)
        if age < 18:
            print("user underage")
        elif 18 < age < 60:
            print("user of age")
        elif 60 < age < 200:
            print("user a senior")
        elif age > 200:
            print("user dead")
    else:
        print("entry empty")
root.title("Age Checker")

ageEntry = tk.Entry(root)
ageEntry.pack()

button = tk.Button(root, text="Underage, Adult, Senior Citizen", command=checkAge)
button.pack()

root.mainloop()