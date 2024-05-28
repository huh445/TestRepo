import tkinter as tk
from tkinter import ttk
from lessons.lessons import Analyse

class AddLesson:
    def __init__(self, id):
        self.id = id

    def add_lesson(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        instrument = self.instrument_entry.get()
        # room = self.room_entry.get()
        combination = self.combination_get.get()
        self.analyse.add_lesson(name, date, time, instrument, combination, str(self.id))

    def actual(self, id):
        self.root = tk.Tk()
        self.root.geometry("640x480")
        self.id = id

        self.analyse = Analyse()
        self.name_label = tk.Label(self.root, text="Student Name:")
        self.name_entry = tk.Entry(self.root)
        self.date_label = tk.Label(self.root, text="Date:")
        self.date_entry = tk.Entry(self.root)
        self.time_label = tk.Label(self.root, text="Time:")
        self.time_entry = tk.Entry(self.root)
        self.instrument_label = tk.Label(self.root, text="Instrument:")
        self.instrument_entry = tk.Entry(self.root)
        self.room_entry = tk.Entry(self.root)
        self.combination_label = tk.Label(self.root, text="Has student prepaid?")
        self.combination_get = ttk.Combobox(self.root, values=["True", "False"])
        self.add_lesson_button =  tk.Button(self.root, text="Add Lesson", command=self.add_lesson)

        self.combination_get.current(0)

        self.pack()

    def pack(self):
        self.name_label.pack()
        self.name_entry.pack()
        self.date_label.pack()
        self.date_entry.pack()
        self.time_label.pack()
        self.time_entry.pack()
        self.instrument_label.pack()
        self.instrument_entry.pack()
        # self.room_entry.pack()
        self.combination_label.pack()
        self.combination_get.pack()
        self.add_lesson_button.pack()
        self.root.mainloop()