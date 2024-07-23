import tkinter as tk
from tkinter import messagebox
from login.validate import Validate
from timetable import Timetable

class Login:
    def __init__(self):
        self.root = tk.Tk()

        self.validate = Validate()

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)

        self.pack()
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        validate, staff, id = self.validate.login(username, password)
        if validate == True:
            if staff == True:
                self.root.destroy()
                Timetable(id, staff)
            elif staff == False:
                self.root.destroy()
                Timetable(id, staff)
        else:
            messagebox.showerror("Error", "Username or Password incorrect")

    def pack(self):
        self.root.geometry("640x480")

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

        self.root.mainloop()