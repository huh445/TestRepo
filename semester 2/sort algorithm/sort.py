import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("400x300")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me")
button.pack(pady=20)

root.mainloop()
