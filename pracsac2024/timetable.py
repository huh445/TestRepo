import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from login.change_password import PasswordChanger
from lessons.lessons import Analyse
from lessons.add_lesson import AddLesson

class Timetable:
    def __init__(self, id, staff):
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("Time", "Name", "Instrument")
        self.validate = Analyse()
        self.add_lesson = AddLesson(id)
        self.id = id
        self.staff = staff
        self.root.geometry("800x400")
        self.search_entry = tk.Entry(self.root)
        self.search_button = tk.Button(self.root, text="Search Dates", command=self.search)
        self.change_pass_button = tk.Button(self.root, text="Change Password", command=self.change_password)
        self.add_booking_button = tk.Button(self.root, text="Add Booking", command=self.add_booking)
        self.logout_button = tk.Button(self.root, text="Logout", command=lambda: self.root.destroy())
        self.display_tree()
        self.pack()

    def display_tree(self):
        self.tree.heading("#0", text="Date")
        for col in ("Time", "Name", "Instrument"):
            self.tree.heading(col, text=col)
        rows, col = self.validate.get_lessons(self.id)
        for row, date in zip(rows, col):
            self.tree.insert("", tk.END, text=date, values=row)

    def add_booking(self):
        self.add_lesson.actual()

    def search(self):
        date = self.search_entry.get()
        self.tree.delete(*self.tree.get_children())
        rows, col = self.validate.search(date)
        for row, date in zip(rows, col):
            self.tree.insert("", tk.END, text=date, values=row)

    def change_password(self):
        if self.staff == True:
            PasswordChanger(self.id)
        else:
            messagebox.showerror("Error", "Permission Denied")

    def pack(self):
        self.change_pass_button.pack()
        self.search_entry.pack()
        self.search_button.pack()
        self.add_booking_button.pack()
        self.tree.pack()
        self.logout_button.pack()
        self.root.mainloop()
if __name__ == "__main__":
    john = Timetable(1, True)