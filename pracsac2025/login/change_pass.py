import tkinter as tk
from tkinter import messagebox
from login.validate import Validate

class PasswordChanger:
    def __init__(self):
        self.validate = Validate()

    def actual(self, id):
        self.root = tk.Tk()

        self.id = id

        self.password_entry = tk.Entry(self.root)
        self.password_button = tk.Button(self.root, text="Change Password", command=self.change_password)
        self.pack()

    def change_password(self):
        password = self.password_entry.get()
        if len(password) == 5:
            self.validate.change_password(password, self.id)
        else:
            messagebox.showerror("Error", "Password has to be 5 characters.")
    
    def pack(self):
        self.root.geometry("640x480")
        self.password_entry.pack()
        self.password_button.pack()