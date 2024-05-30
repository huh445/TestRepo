import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def addPokemon():
    name = pokemonEntryName.get()
    type = pokemonEntryType.get()
    if name and type:
        textDisplay.delete(1.0, tk.END)
        text = f"The Pork name is {name} with typing {type}"
        textDisplay.insert(tk.END, text)
    else:
        messagebox.showwarning("Error", "One or more of the boxes is empty.")

root.title("Pork")

root.geometry("640x480")

root.configure(bg="blue")

pokemonEntryName = tk.Entry(root)
pokemonEntryName.pack(pady=5)
pokemonEntryName.configure(bg="blue", fg="white")

pokemonEntryType = tk.Entry(root)
pokemonEntryType.pack(pady=5)
pokemonEntryType.configure(bg="blue", fg="white")

addPokemonData = tk.Button(root, text="Add the Pork data", command=addPokemon)
addPokemonData.pack()
addPokemonData.configure(pady=5, bg="blue", fg="white")

textDisplay = tk.Text(root)
textDisplay.pack()
textDisplay.configure(bg="blue", fg="white")

root.mainloop()