import tkinter as tk
from tkinter import ttk
from import_csv import ImportCSV

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root)
        
        self.importcsv = ImportCSV()

        self.import_csv_button = tk.Button(self.root, text="Import CSV to tree", command=self.import_csv)
        self.run()
    def import_csv(self):
        headers, rows = self.importcsv.import_csv()
        for header in headers:
            self.tree.heading(header, values=header)
            self.tree.column(header)
        for row in rows:
            self.tree.insert("", tk.END, values=row)
    def run(self):
        self.import_csv_button.pack()
        self.tree.pack()
        self.root.mainloop()