import tkinter as tk

# Create a Tkinter root
root = tk.Tk()
root.title("Pokédex") 

# Create GUI components
label_title = tk.Label(root, text="Pokédex", font=("Arial", 24))
label_title.pack()
label_title.configure(font=("Arial", 24), fg="White", bg="red", pady=10)

label_instructions = tk.Label(root, text="Enter Pokémon Name:")
label_instructions.pack()
label_instructions.configure(bg="red", pady=5, fg="white")

entry_name = tk.Entry(root)
entry_name.pack(pady=5)

root.configure(bg="red")

button_search = tk.Button(root, text="Search")
button_search.pack()
button_search.configure(bg="white", pady=5)

label_result = tk.Label(root, text="Pokémon Information:")
label_result.pack()
label_result.configure(bg="red", pady=5, fg="white")

text_display = tk.Text(root, height=6, width=30)
text_display.pack(pady=5    )

root.geometry("400x300")
root.title("Pokedex")

# Function to display Pokémon information
def display_pokemon_info():
    pokemon_name = entry_name.get()
    # Fetch Pokémon information from database or API
    pokemon_info = f"Name: {pokemon_name}\nType: Fire\nHeight: 1.2m\nWeight: 35.0kg"
    text_display.delete(1.0, tk.END)  # Clear previous text
    text_display.insert(tk.END, pokemon_info)

# Bind button click event to display_pokemon_info function
button_search.config(command=display_pokemon_info)

# Run the Tkinter event loop
root.mainloop()
