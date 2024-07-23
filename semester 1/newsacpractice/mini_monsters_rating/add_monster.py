import tkinter as tk
from open_xml import OpenXML

class AddMonster:
    def __init__(self):
        self.root = tk.Tk()
        self.xml = OpenXML()


        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)

        self.type_label = tk.Label(self.root, text="Type:")
        self.type_entry = tk.Entry(self.root)

        self.weight_label = tk.Label(self.root, text="Weight:")
        self.weight_entry = tk.Entry(self.root)

        self.colour_label = tk.Label(self.root, text="Colour:")
        self.colour_entry = tk.Entry(self.root)
        self.add_monster_button = tk.Button(self.root, text="Add monster", command=self.add_monster)

        self.pack()

    def add_monster(self):

        id = self.xml.highest_rank()

        name = self.name_entry.get().lower()
        type = self.type_entry.get().lower()
        weight = self.weight_entry.get().lower()
        colour = self.colour_entry.get().lower()

        data = {"rank": id,"name": name, "type": type, "weight": weight, "colour": colour}
        self.root.destroy()
        self.xml.add_monsters(data)

    def pack(self):
        self.root.geometry("640x480")
        self.name_label.pack()
        self.name_entry.pack()
        
        self.type_label.pack()
        self.type_entry.pack()
        
        self.weight_label.pack()
        self.weight_entry.pack()
        
        self.colour_label.pack()
        self.colour_entry.pack()
        
        self.add_monster_button.pack()
        self.root.mainloop()