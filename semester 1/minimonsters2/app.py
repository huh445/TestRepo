import tkinter as tk
from monsterimport import Search
from add import Add

class App:
    def __init__(self, root, tree):
        self.root = root
        self.tree = tree
        self.filename = "monsters.csv"
        self.csv = Search(self.filename)

        self.entry = tk.Entry(self.root)
        self.entry_search = tk.Button(self.root, text="Search the database", command=self.search_csv)
        self.sort_alpha_button = tk.Button(self.root, text="Search Alphabetically", command=self.sort_alpha)
        self.sort_num_button = tk.Button(self.root, text="Search Numerically", command=self.sort_num)
        self.add_data_button = tk.Button(self.root, text="Add Data", command=self.add_data)
        self.import_csv()
        self.styles()
    def search_csv(self):
        key = self.entry.get()
        headers, rows = self.csv.search_filter(key)
        self.display_tree(headers, rows)

    def import_csv(self):
        headers, rows = self.csv.import_csv()
        self.tree["columns"] = headers
        self.display_tree(headers, rows)
    def sort_alpha(self):
        headers, rows = self.csv.sort_alpha()
        self.display_tree(headers, rows)
    def sort_num(self):
        headers, rows = self.csv.sort_num()
        self.display_tree(headers, rows)
    def display_tree(self, headers, rows):
        self.tree.delete(*self.tree.get_children())
        for header in headers:
            self.tree.heading(header, text=header)
            self.tree.column(header)
        for row in rows:
            self.tree.insert("", tk.END, value=row)
    def add_data(self):
        self.add = Add(self.filename)
        self.add.add_monster_button()
        self.sort_num()
    def styles(self):
        self.tree.pack()
        self.entry.pack()
        self.entry_search.pack()
        self.sort_alpha_button.pack()
        self.sort_num_button.pack()
        self.add_data_button.pack()