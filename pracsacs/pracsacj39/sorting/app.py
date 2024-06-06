import tkinter as tk
from tkinter import ttk
from csv_reader import CSVReader
from sort import Sort

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.csv = CSVReader()
        self.sort = Sort()
        self.tree = ttk.Treeview(self.root)
        self.sort_subject_button = tk.Button(self.root, text="Sort by Subject", command=self.sort_subject)
        self.sort_textbook_button = tk.Button(self.root, text="Sort by Textbook", command=self.sort_textbook)
        self.sort_rating_button = tk.Button(self.root, text="Sort by Rating", command=self.sort_rating)
        self.quit_button = tk.Button(self.root, text="Quit", command=lambda: self.root.destroy())
        self.import_tree()
        self.run()
    
    def import_tree(self):
        headers, rows = self.csv.read_csv()
        self.headers, self.rows = headers, rows
        self.tree["columns"] = headers
        self.update_tree(rows)

    def sort_subject(self):
        rows = self.sort.sort_subject(self.rows)
        self.update_tree(rows)
    
    def sort_textbook(self):
        rows = self.sort.sort_textbook(self.rows)
        self.update_tree(rows)
    
    def sort_rating(self):
        rows = self.sort.sort_rating(self.rows)
        self.update_tree(rows)

    def update_tree(self, rows):
        self.tree.delete(*self.tree.get_children())
        for header in self.headers:
            self.tree.heading(header, text=header)
            self.tree.column(header)
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def run(self):
        self.tree.pack()
        self.sort_subject_button.pack()
        self.sort_textbook_button.pack()
        self.sort_rating_button.pack()
        self.quit_button.pack()
        self.root.mainloop()