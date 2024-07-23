import tkinter as tk
from tkinter import messagebox
class app:
    def __init__(self, master):
        self.master = master
        tkinter.__init__(self)
    def destroy(self):
        self.master.destroy()

class tkinter(app):
    def __init__(self):
        self.master.title("John Smith 2")
        self.master.geometry("640x480")

        self.button = tk.Button(self.master, text="Sex 2", command=self.destroy)
        self.button.pack()
def main():
    root = tk.Tk()
    application = app(root)
    root.mainloop()
if __name__ == "__main__":
    main()