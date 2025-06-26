import tkinter as tk

root = tk.Tk()
root.title("John")

def text_appear():
    label.pack()

button = tk.Button(root, text="John B Edwards", command=text_appear)
button.pack()

label = tk.Label(root, text="Hi!")

root.geometry("360x640")

root.mainloop()