import tkinter as tk
from tkinter import messagebox
from login.change_password import PasswordChanger

class Timetable:
    def __init__(self, id, staff):
        self.root = tk.Tk()
        self.id = id
        self.staff = staff

        self.root.geometry("640x480")
        self.change_pass_button = tk.Button(self.root, text="Change Password", command=self.change_password)
        self.pack()
    def change_password(self):
        if self.staff == True:
            PasswordChanger(self.id)
        else:
            messagebox.showerror("Error", "Permission Denied")
    def pack(self):
        self.change_pass_button.pack()
        self.root.mainloop()