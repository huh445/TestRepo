import tkinter as tk
from tkinter import ttk, messagebox
from importcsv import ImportCSV

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root)
        self.import_csv = ImportCSV()

        self.tree_button = tk.Button(self.root, text="Import Data", command=self.tree_init)

        self.run()

    def tree_init(self):
        headers, rows = self.import_csv.import_csv()

        self.tree["columns"] = headers

        for header in headers:
            self.tree.heading(header, values=header)
            self.tree.column(header)
        
        for row in rows:
            self.tree.insert("", tk.END, values=row)
    
    def run(self):
        self.tree_button.pack()
        self.tree.pack()

        self.root.mainloop()