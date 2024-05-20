import tkinter as tk
from tkinter import ttk
import csv
class App:
    def __init__(self, root, tree):
        self.root = root
        self.tree = tree

        self.tree["columns"] = ("Number", "Type", "Height", "Weight")
        self.configureHeadings()

        self.importcsv()
        self.data = self.getValues()

        self.sortNameButton = tk.Button(self.root, text="Sort by Name", command=self.sortName)
        self.sortNumButton = tk.Button(self.root, text="Sort by Number", command=self.sortNumber)

        self.sortNameButton.pack()
        self.sortNumButton.pack()
        self.tree.pack(pady=10)

    def configureHeadings(self):
        self.tree.heading("#0", Text="Name")
        for col in ("Number", "Type", "Height", "Weight"):
            self.tree.heading(col, text=col)

    def importcsv(self):
        with open("C:\jhon.csv", "r") as f:
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

if __name__ == "__main__":
    root = tk.Tk()
    tree = ttk.Treeview(root)
    application = App(root, tree)
    root.mainloop()
