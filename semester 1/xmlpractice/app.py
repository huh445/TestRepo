import tkinter as tk
from tkinter import ttk
from monsterimport import Import

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root)
        self.import_monster =  Import()

        self.display_button = tk.Button(self.root, text="Display to tree", command=self.display)

    def display(self):
        headers, rows = self.import_monster.import_csv()

        self.tree["columns"] = headers

        for header in headers:
            self.tree.heading(header, text=header)
            self.tree.column(header)
        
        for row in rows:
            self.tree.