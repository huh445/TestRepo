import tkinter as tk
from tkinter import messagebox
from timetable import Timetable
from login.validate import Validate

class Login:
    def __init__(self, root):
        self.root = root
        self.validate = Validate()
        self.username = tk.Entry(self.root)
        self.password = tk.Entry(self.root)

        self.login_button = tk.Button(self.root, text="Login", command=self.goto_validate)

        self.pack()
    def goto_validate(self):
        username = self.username.get()
        password = self.password.get()
        if self.validate.login(username, password) == True:
            self.root.destroy()
            messagebox.showinfo("Success", "Successful Login.")
            Timetable()
        else:
            print(False)
    def pack(self):
        self.root.geometry("640x480")
        self.username.pack()
        self.password.pack()
        self.login_button.pack()