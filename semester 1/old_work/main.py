import tkinter as tk
from tkinter import ttk
import csv
class App:
    def __init__(self, root, tree):
        self.root = root
        self.tree = tree
        self.root.title("Mini Monsters Index")

        self.tree["columns"] = ("Number", "Type", "Height", "Weight")
        self.configureHeadings()

        self.sortNameButton = tk.Button(self.root, text="Sort by Name", command=self.sortName)
        self.sortNumButton = tk.Button(self.root, text="Sort by Number", command=self.sortNumber)
        self.title = tk.Label(self.root, text="Mini Monsters Index")

        self.importcsv()
        self.data = self.getValues()
        self.styles()

    def configureHeadings(self):
        self.tree.heading("#0", text="Name")
        for col in ("Number", "Type", "Height", "Weight"):
            self.tree.heading(col, text=col)

    def importcsv(self):
        with open("monsters.csv", "r") as f:
            self.csvreader = csv.DictReader(f)
            for row in self.csvreader:
                name = row["Name"]
                self.tree.insert("", tk.END, text=name, values=(row["Number"], row["Type"], row["Height"], row["Weight"]))

    def sortName(self):
        sortedMonster = sorted(self.data.items())
        self.updateTreeView(sortedMonster)

    def sortNumber(self):
        sortedMonster = sorted(self.data.items(), key=lambda x: x[1]["Number"])
        self.updateTreeView(sortedMonster)

    def getValues(self):
        allData = {}
        for item in self.tree.get_children():
            name = self.tree.item(item, "text")
            allValues = self.tree.item(item, "values")

            data = {}
            data["Number"] = int(allValues[0])
            data["Type"] = allValues[1]
            data["Height"] = allValues[2]
            data["Weight"] = allValues[3]

            allData[name] = data
        return allData
    
    def updateTreeView(self, sortedMonster):
        self.tree.delete(*self.tree.get_children())
        for name, info in sortedMonster:
            self.tree.insert("", "end", text=name, values=(info["Number"], info["Type"], info["Height"], info["Weight"]))
    
    def styles(self):
        self.root.config(bg="blue")
        self.title.config(bg="blue", font=("Arial", 24), fg="white")
        self.sortNameButton.config(bg="blue", fg="white")
        self.sortNumButton.config(bg="blue", fg="white")
        self.title.pack(pady=10)
        self.tree.pack(pady=10)
        self.sortNameButton.pack(side="left", pady=10, padx=5)
        self.sortNumButton.pack(side="left", pady=10, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    tree = ttk.Treeview(root)
    application = App(root, tree)
    root.mainloop()
