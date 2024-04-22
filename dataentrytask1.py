import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("800x600")
pokemonList = {
    "John": "Balls"
}

def add_pokemon():
    pokemonEntryName = pokemonName.get()
    pokemonEntryType = pokemonType.get()r
    if pokemonEntryName and pokemonEntryType:
        pokemonList[pokemonEntryName] = pokemonEntryType
        print(pokemonList)
        print(f"{pokemonEntryName} with typing {pokemonEntryType
                                                }")
    else:
       error = "One or both of the fields are empty."
       messagebox.showwarning("Error", error)


pokemonName = tk.Entry(root)
pokemonName.pack()

pokemonType = tk.Entry(root)
pokemonType.pack()

entryButton = tk.Button(root, text="Enter the pokemon into the pokedex.", command=add_pokemon)
entryButton.pack()

root.title("Pokedex Entry")

root.mainloop()