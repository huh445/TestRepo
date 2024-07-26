import tkinter as tk

def display_monster_info():
    monster_name = entry_name.get()
    # Fetch Mini Monsters information from database or API
    monster_info = f"Name: {monster_name}\nType: Fire\nHeight: 1.2m\nWeight: 35.0kg"
    text_display.delete(1.0, tk.END)  # Clear previous text
    text_display.insert(tk.END, monster_info)

root = tk.Tk()
root.geometry("400x300")
root.configure(bg="blue")
root.title("Mini Monsters Index")

label_title = tk.Label(root, text="Mini Monsters Index")
label_title.pack()
label_title.configure(font=("Arial", 24), bg="blue", fg="white", pady=10)

label_instructions = tk.Label(root, text="Enter Mini Monster Name:")
label_instructions.pack()
label_instructions.configure(bg="blue", fg="white", pady=5)

entry_name = tk.Entry(root)
entry_name.pack(pady=5)

button_search = tk.Button(root, text="Search", command=display_monster_info)
button_search.pack(pady=5)
button_search.configure(bg="white")

label_result = tk.Label(root, text="Mini Monster Information:")
label_result.pack()
label_result.configure(bg="blue", fg="white", pady=5)

text_display = tk.Text(root, height=6, width=40)
text_display.pack()
text_display.configure(bg="white", pady=5)


root.mainloop()
