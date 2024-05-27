import tkinter as tk
from tkinter import messagebox
from login.validate import Validate

class PasswordChanger:
    def __init__(self, id):
        self.id = id
        self.validate = Validate()
        self.root = tk.Tk()

        self.entry = tk.Entry(self.root)
        self.change_pass = tk.Button(self.root, text="Change Password", command=self.change)
        self.pack()
    def change(self):
        password = self.entry.get()
        if len(password) == 5:
            self.validate.change_password(self.id, password)
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Password needs to be 5 characters.")
    def pack(self):
        self.entry.pack()
        self.change_pass.pack()