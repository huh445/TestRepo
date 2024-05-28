import tkinter as tk
from tkinter import ttk
from lessons.lessons import Analyse
from lessons.rooms import ImportRooms

class AddLesson:
    def __init__(self, id):
        self.id = id

    def add_lesson(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        instrument = self.instrument_entry.get()
        combination = self.combination_get.get()
        rooms = self.room_combination.get()
        self.analyse.add_lesson(name, date, time, instrument, combination, rooms, str(self.id))
        self.root.destroy()
    
    def get_rooms(self):
        rooms = self.import_rooms.all_rooms()
        return rooms

    def actual(self, id):
        self.root = tk.Tk()
        self.root.geometry("640x480")
        self.id = id

        self.import_rooms = ImportRooms()
        rooms = self.get_rooms()
        self.analyse = Analyse()
        self.name_label = tk.Label(self.root, text="Student Name:")
        self.name_entry = tk.Entry(self.root)
        self.date_label = tk.Label(self.root, text="Date:")
        self.date_entry = tk.Entry(self.root)
        self.time_label = tk.Label(self.root, text="Time:")
        self.time_entry = tk.Entry(self.root)
        self.instrument_label = tk.Label(self.root, text="Instrument:")
        self.instrument_entry = tk.Entry(self.root)
        self.combination_label = tk.Label(self.root, text="Has student prepaid?")
        self.combination_get = ttk.Combobox(self.root, values=["True", "False"])
        self.room_label = tk.Label(self.root, text="Room:")
        self.room_combination = ttk.Combobox(self.root, values=rooms)
        self.add_lesson_button =  tk.Button(self.root, text="Add Lesson", command=self.add_lesson)

        self.combination_get.current(0)

        self.room_combination.current(0)

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
        self.combination_label.pack()
        self.combination_get.pack()
        self.add_lesson_button.pack()
        self.room_label.pack()
        self.room_combination.pack()
        self.root.mainloop()