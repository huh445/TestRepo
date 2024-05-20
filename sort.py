import tkinter as tk
from tkinter import ttk

root = tk.Tk()

pokemonData = {
"Bulbasaur": {"Number": 1, "Type": "Grass/Poison", "Height": "0.7m", "Weight": "6.9kg"},
"Ivysaur": {"Number": 2, "Type": "Grass/Poison", "Height": "1.0m", "Weight": "13.0kg"},
"Venusaur": {"Number": 3, "Type": "Grass/Poison", "Height": "2.0m", "Weight": "100.0kg"},
"Charmander": {"Number": 4, "Type": "Fire", "Height": "0.6m", "Weight": "8.5kg"},
"Charmeleon": {"Number": 5, "Type": "Fire", "Height": "1.1m", "Weight": "19.0kg"},
"Charizard": {"Number": 6, "Type": "Fire/Flying", "Height": "1.7m", "Weight": "90.5kg"},
"Squirtle": {"Number": 7, "Type": "Water", "Height": "0.5m", "Weight": "9.0kg"},
"Wartortle": {"Number": 8, "Type": "Water", "Height": "1.0m", "Weight": "22.5kg"},
"Blastoise": {"Number": 9, "Type": "Water", "Height": "1.6m", "Weight": "85.5kg"},
"Caterpie": {"Number": 10, "Type": "Bug", "Height": "0.3m", "Weight": "2.9kg"},
"Metapod": {"Number": 11, "Type": "Bug", "Height": "0.7m", "Weight": "9.9kg"},
"Butterfree": {"Number": 12, "Type": "Bug/Flying", "Height": "1.1m", "Weight": "32.0kg"},
"Weedle": {"Number": 13, "Type": "Bug/Poison", "Height": "0.3m", "Weight": "3.2kg"},
"Kakuna": {"Number": 14, "Type": "Bug/Poison", "Height": "0.6m", "Weight": "10.0kg"},
"Beedrill": {"Number": 15, "Type": "Bug/Poison", "Height": "1.0m", "Weight": "29.5kg"},
"Pidgey": {"Number": 16, "Type": "Normal/Flying", "Height": "0.3m", "Weight": "1.8kg"},
"Pidgeotto": {"Number": 17, "Type": "Normal/Flying", "Height": "1.1m", "Weight": "30.0kg"},
"Pidgeot": {"Number": 18, "Type": "Normal/Flying", "Height": "1.5m", "Weight": "39.5kg"},
# Add more Pokémon data here
}

root.title("Pokédex")
root.geometry("640x480")

def sortByNumber():
    sortedPokemon = sorted(pokemonData.items(), key=lambda x: x[1]["Number"])
    tree.delete(*tree.get_children())
    for pokemon, info in sortedPokemon:
        tree.insert("", "end", text=pokemon, values=(info["Number"], info["Type"], info["Height"], info["Weight"]))

def sortAlphabetically():
        sortedPokemon = sorted(pokemonData.items())
        tree.delete(*tree.get_children())
        for pokemon, info in sortedPokemon:
            tree.insert("", "end", text=pokemon, values=(info["Number"], info["Type"], info["Height"], info["Weight"]))

def sortWeight():
    sortedPokemon = sorted(pokemonData.items(), key=lambda x: float(x[1]["Weight"].split("kg")[0]))
    tree.delete(*tree.get_children())
    for pokemon, info in sortedPokemon:
        tree.insert("", "end", text=pokemon, values=(info["Number"], info["Type"], info["Height"], info["Weight"]))

tree = ttk.Treeview(root)
tree["columns"] = ("Number", "Type", "Height", "Weight")
tree.heading("#0", text="Name")
tree.heading("Number", text="Number")
tree.heading("Type", text="Type")
tree.heading("Height", text="Height")
tree.heading("Weight", text="Weight")

for pokemon, info in pokemonData.items():
    tree.insert("", "end", text=pokemon, values=(info["Number"], info["Type"], info["Height"], info["Weight"]))


buttonSortNumber = tk.Button(root, text="Sort Numerically", command=sortByNumber)
buttonSortNumber.pack(pady=5)

buttonSortAlpha = tk.Button(root, text="Sort Alphabetically", command=sortAlphabetically)
buttonSortAlpha.pack(pady=5)

buttonSortWeight = tk.Button(root, text="Sort By Weight", command=sortWeight)
buttonSortWeight.pack(pady=5)

tree.pack(pady=10)
root.mainloop()