import tkinter as tk
from tkinter import ttk
from csv_import import ImportCSV
from sort_ticket import Sort

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.csv = ImportCSV()
        self.tree = ttk.Treeview(self.root)
        self.sort_id = tk.Button(self.root, text="Sort by ID", command=self.sort_ticket)
        self.search_entry = tk.Entry(self.root)
        self.search_button = tk.Button(self.root, text="Sort by status", command=self.sort_search)
        self.sort = Sort()
        self.import_csv()
        self.pack()
    def import_csv(self):
        headers, rows = self.csv.import_csv()
        self.tree["columns"] = headers
        self.rows = rows
        self.headers = headers
        self.update_tree(headers, rows)
    
    def sort_ticket(self):
        rows, headers = self.sort.sort_ticket(self.rows, self.headers)
        self.update_tree(headers, rows)

    def update_tree(self, headers, rows):
        self.tree.delete(*self.tree.get_children())
        for header in headers:
            self.tree.heading(header, text=header)
            self.tree.column(header)
        for row in rows:
            self.tree.insert("", tk.END, values=row)
    
    def sort_search(self):
        key = self.search_entry.get()
        rows, headers = self.sort.sort_search(self.rows, self.headers, key)
        self.update_tree(headers, rows)
    
    def pack(self):
        self.tree.pack()
        self.sort_id.pack()
        self.search_entry.pack()
        self.search_button.pack()

        self.root.mainloop()