import tkinter as tk
from monsterimport import Search

class Add:
    def __init__(self, filename):
        self.root = tk.Tk()
        self.csv = Search(filename)

        self.data = []

        self.name = tk.Entry(self.root)
        self.type = tk.Entry(self.root)
        self.height = tk.Entry(self.root)
        self.weight = tk.Entry(self.root)
        self.add = tk.Button(self.root, text="Add", command=self.add_monster)

    def add_monster(self):
        max_id = self.csv.highest_monster()
        self.data.append(self.name.get())
        self.data.append(max_id + 1)
        self.data.append(self.type.get())
        self.data.append(self.height.get())
        self.data.append(self.weight.get())
        self.root.destroy()
        self.csv.add_data(self.data)
    
    def add_monster_button(self):
        self.styles()
    
    def styles(self):
        self.name.pack()
        self.type.pack()
        self.height.pack()
        self.weight.pack()
        self.add.pack()
        self.root.mainloop()