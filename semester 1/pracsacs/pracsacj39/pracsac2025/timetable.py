import tkinter as tk
from tkinter import ttk
from datetime import date
from login.change_pass import PasswordChanger
from lessons.lessons import Lessons
from lessons.add_lessons import AddLesson

class Timetable:
    def __init__(self, id, staff):
        self.root = tk.Tk()
        self.id = id
        self.staff = staff

        self.password_changer = PasswordChanger()
        self.lessons = Lessons()
        self.add_lessons = AddLesson()

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("Time", "Lessons Missed", "Name", "Instrument", "Room", "Has PrePaid")


        self.search_entry = tk.Entry(self.root)
        self.search_button = tk.Button(self.root, text="Search", command=self.search)
        self.change_pass_button = tk.Button(self.root, text="Change Password", command=self.change_pass)
        self.add_lesson_button = tk.Button(self.root, text="Add a Lesson", command=self.add_lesson)
        
        self.init_tree()
        self.get_date()
        self.pack()
    
    def init_tree(self):
        self.tree.heading("#0", text="Date")
        for cols in ("Time", "Lessons Missed", "Name", "Instrument", "Room", "Has PrePaid"):
            self.tree.heading(cols, text=cols)

    def get_date(self):
        rows, cols = self.lessons.search(date.today(), self.id)
        self.update_tree(rows, cols)

    def search(self):
        rows, cols = self.lessons.search(self.search_entry.get(), self.id)
        self.update_tree(rows, cols)

    def update_tree(self, rows, cols):
        self.tree.delete(*self.tree.get_children())
        for row, col in zip(rows, cols):
            self.tree.insert("", tk.END, text=col, values=row)

    def change_pass(self):
        self.password_changer.actual(self.id)
    
    def add_lesson(self):
        self.add_lessons.actual(self.id)

    def pack(self):
        self.root.geometry("1400x400")
        self.search_entry.pack()
        self.search_button.pack()
        self.change_pass_button.pack()
        self.add_lesson_button.pack()
        self.tree.pack()
        self.root.mainloop()

if __name__ == "__main__":
    john = Timetable(1, True)