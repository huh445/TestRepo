import tkinter as tk
from tkinter import messagebox
from timetable import Timetable

class Login:
    def __init__(self, root, xml):
        self.root = root
        self.xml = xml

        self.username = tk.Entry(self.root)
        self.password = tk.Entry(self.root)

        self.login_button = tk.Button(self.root, text="Login", command=self.validate)

        self.pack()
    def validate(self):
        username = self.username.get()
        password = self.password.get()
        xml_root = self.xml.getroot()
        users = xml_root.findall("user")
        if len(username) == 5 and len(password) == 5:
            for user in users:
                username_element = user.find("username")
                if username_element.text == username:
                    password_element = user.find("password")
                    if password_element.text == password:
                        self.root.destroy()
                        messagebox.showinfo("Success", "Successful Login.")
                        Timetable()
        else:
            print(f"username needs to be 5 characters or more,\nusername is {len(username)} and password is {len(password)} characters long")
    def pack(self):
        self.root.geometry("640x480")
        self.username.pack()
        self.password.pack()
        self.login_button.pack()