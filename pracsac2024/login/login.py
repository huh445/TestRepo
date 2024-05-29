import tkinter as tk
from tkinter import messagebox
from timetable import Timetable
from login.validate import Validate
from login.get_welcome import GetWelcome

class Login:
    def __init__(self, root):
        self.root = root
        self.get_welcome = GetWelcome()
        self.validate = Validate()
        self.title = tk.Label(self.root, text="Welcome to Maestro")
        self.welcome_message = tk.Label(self.root, text=self.get_welcome.get_text())
        self.username_text = tk.Label(self.root, text="Username")
        self.username = tk.Entry(self.root)
        self.password_text = tk.Label(self.root, text="Password")
        self.password = tk.Entry(self.root)

        self.login_button = tk.Button(self.root, text="Login", command=self.goto_validate)

        self.pack() 

    def goto_validate(self):
        username = self.username.get()
        password = self.password.get()
        validate, staff, id = self.validate.login(username, password)
        if staff == True and validate == True:
            self.root.destroy()
            Timetable(id, staff)
        elif validate == True:
            self.root.destroy()
            Timetable(id, staff)
        else:
            print(False)
            
    def pack(self):
        self.root.title("Maestro - please login")
        self.root.geometry("640x480")
        self.title.pack(pady=10, anchor="center")
        self.welcome_message.pack(pady=5, anchor="center")
        self.username_text.pack(pady=5, anchor="center")
        self.username.pack(pady=5, anchor="center")
        self.password_text.pack(pady=5, anchor="center")
        self.password.pack(pady=5, anchor="center")
        self.login_button.pack(pady=10, anchor="center")

        self.title.configure(font=("Arial", 20), fg="black")
        self.welcome_message.configure(font=("Arial", 12), fg="black")
        self.username_text.configure(font=("Arial", 16), fg="black")
        self.username.configure(font=("Arial", 16), fg="black")
        self.password_text.configure(font=("Arial", 16), fg="black")
        self.password.configure(font=("Arial", 16), fg="black")
        self.login_button.configure(font=("Arial", 18), fg="white", bg="black")