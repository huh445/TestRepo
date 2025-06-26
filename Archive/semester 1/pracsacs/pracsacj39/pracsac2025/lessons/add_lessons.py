import tkinter as tk
from tkinter import ttk
from lessons.lessons import Lessons
from lessons.rooms import Rooms

class AddLesson:
    def __init__(self):
        self.lessons = Lessons()
        self.rooms = Rooms()
    def actual(self, id):
        self.root = tk.Tk()
        self.root.geometry("640x480")

        rooms = self.rooms.get_rooms()
        self.id = id
        
        self.name_label = tk.Label(self.root, text="Student Name:")
        self.name_entry = tk.Entry(self.root)
        self.date_label = tk.Label(self.root, text="Date of Lesson:")
        self.date_entry = tk.Entry(self.root)
        self.time_label = tk.Label(self.root, text="Time of lesson:")
        self.time_entry = tk.Entry(self.root)
        self.instrument_label = tk.Label(self.root, text="Instrument:")
        self.instrument_entry = tk.Entry(self.root)
        self.room_label = tk.Label(self.root, text="Room:")
        self.room_combo = ttk.Combobox(self.root, values=rooms)
        self.paid_label = tk.Label(self.root, text="Has the student paid?")
        self.paid_combo = ttk.Combobox(self.root, values=["True", "False"])
        self.lessons_missed_label = tk.Label(self.root, text="How many lessons has the student missed?")
        self.lessons_missed_entry = tk.Entry(self.root)

        self.button = tk.Button(self.root, text="Add Lesson", command=self.add_lesson)

        self.pack()

    def add_lesson(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        instrument = self.instrument_entry.get()
        room = self.room_combo.get()
        paid = self.paid_combo.get()
        lessons_missed = self.lessons_missed_entry.get()
        lesson_data = {"student": name, "date":date, "time":time, "instrument":instrument, "roomid":room, "has_paid":paid, "lessons_missed":lessons_missed, "teacherid":self.id}
        self.lessons.add_lessons(lesson_data)
        self.root.destroy()

    def pack(self):
        self.name_label.pack()
        self.name_entry.pack()
        self.date_label.pack()
        self.date_entry.pack()
        self.time_label.pack()
        self.time_entry.pack()
        self.instrument_label.pack()
        self.instrument_entry.pack()
        self.room_label.pack()
        self.room_combo.pack()
        self.paid_label.pack()
        self.paid_combo.pack()
        self.lessons_missed_label.pack()
        self.lessons_missed_entry.pack()
        self.button.pack()

        self.root.mainloop()