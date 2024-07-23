import tkinter as tk
from tkinter import ttk
from open_xml import OpenXML
from add_monster import AddMonster

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.xml = OpenXML()
        self.tree = ttk.Treeview(self.root)
        self.add_monster_button = tk.Button(self.root, text="Add Monster", command=self.add_monster)
        self.init_tree()
        self.pack()

    def init_tree(self):
        self.tree["column"] = ["Name", "Type", "Weight", "Colour"]
        self.tree.heading("#0", text="Rank")
        for col in ("Name", "Type", "Weight", "Colour"):
            self.tree.heading(col, text=col)
        rows, cols = self.xml.get_monsters()
        self.update_tree(rows, cols)

    def update_tree(self, rows, cols):
        self.tree.delete(*self.tree.get_children())
        for row, col in zip(rows, cols):
            self.tree.insert("", tk.END, text=col, values=row)

    def add_monster(self):
        AddMonster()
        rows, cols = self.xml.get_monsters()
        self.update_tree(rows, cols)

    def pack(self):
        self.add_monster_button.pack()
        self.tree.pack()
        self.root.mainloop()