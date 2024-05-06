import tkinter as tk
from tkinter import ttk

root = tk.Tk()

pokemonData = {
"Bulbasaur": {"Number": 1, "Type": "Grass/Poison", "Height": "0.7m", "Weight": "6.9kg"},
"Ivysaur": {"Number": 2, "Type": "Grass/Poison", "Height": "1.0m", "Weight": "13.0kg"},
"Venusaur": {"Number": 3, "Type": "Grass/Poison", "Height": "2.0m", "Weight": "100.0kg"},
}

root.title("Pokédex")
root.geometry("640x480")

tree = ttk.Treeview(root)
tree["columns"] = ("Number", "Type", "Height", "Weight")
tree.heading("#0", text="Name")
tree.heading("Number", text="Number")
tree.heading("Type", text="Type")
tree.heading("Height", text="Height")
tree.heading("Weight", text="Weight")

for pokemon, info in pokemonData.items():
    tree.insert("", "end", text=pokemon, values=(info["Number"], info["Type"], info["Height"], info["Weight"]))
tree.pack(pady=10)
root.mainloop()