import tkinter as tk
from tkinter import ttk
from monsterimport import Search
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root)
        self.root.title("Mini Monsters Index")
        self.csv = Search()
        
        self.sortNameButton = tk.Button(self.root, text="Sort by Name", command=self.sortName)
        self.sortNumButton = tk.Button(self.root, text="Sort by Number", command=self.sortNumber)
        self.title = tk.Label(self.root, text="Mini Monsters Index")
        self.entry = tk.Entry(self.root)
        self.entryButton = tk.Button(self.root, text="Search", command=self.sortEntry)
        self.entryTitle = tk.Label(self.root, text="Search by Name:")

        self.importcsv()
        self.styles()

    def importcsv(self):
        headers, rows = self.csv.import_csv(filename = "monsters.csv")
        self.tree["columns"] = headers
        for header in headers:
            self.tree.heading(header, text=header)
            self.tree.column(header)

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def sortName(self):
        rows, headers = self.csv.sort_name()
        self.updateTreeView(rows, headers)

    def sortNumber(self):
        rows, headers = self.csv.sort_number()
        self.updateTreeView(rows, headers)
    
    def sortEntry(self):
        key = self.entry.get()
        if key:
            rows, headers = self.csv.sort_entry(key)
            self.updateTreeView(rows, headers)
    
    def updateTreeView(self, rows, headers):
        self.tree.delete(*self.tree.get_children())
        for header in headers:
            self.tree.heading(header, text=header)
            self.tree.column(header)

        for row in rows:
            self.tree.insert("", tk.END, values=row)
    
    def styles(self):
        self.root.config(bg="blue")
        self.title.config(bg="blue", font=("Arial", 24), fg="white")
        self.sortNameButton.config(bg="blue", fg="white")
        self.sortNumButton.config(bg="blue", fg="white")
        self.entryButton.config(bg="blue", fg="white")
        self.entryTitle.config(bg="blue", fg="white", font=("Arial", 12))

        self.title.pack(pady=10)
        
        self.entryTitle.pack(pady=5)
        self.entry.pack(pady=5)
        self.entryButton.pack(pady=5)

        self.tree.pack(pady=10, fill=tk.BOTH)
        self.sortNameButton.pack(side="left", pady=10, padx=5)
        self.sortNumButton.pack(side="left", pady=10, padx=5)

        self.root.mainloop()