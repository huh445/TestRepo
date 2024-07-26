import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
import csv

class App:
    def __init__(self, root, style):
        self.root = root
        self.style = style
        self.style.theme_use("alt")

        self.style.configure("Treeview", background="#564D65", foreground="#2CDA9D", font="Abel")
        self.style.configure("Treeview.Heading", background="#564D65", foreground="#2CDA9D", font="Abel")
        self.style.map("Treeview", background=[("selected", "#3E8989")])
        self.style.map("Treeview.Heading", background=[("active", "#3E8989")])

        self.tree = ttk.Treeview(self.root, columns=("Number", "Type", "Height", "Weight"))
        self.configure_headings()
        self.import_csv()


        self.style.configure("TButton", background="#564D65", foreground="#2CDA9D", font="Abel", relief="flat")
        self.style.map("TButton", background=[("active", "#3E8989")])

        self.sort_name_button = ttk.Button(self.root, text="Sort by Name", command=self.sort_name)
        self.sort_num_button = ttk.Button(self.root, text="Sort by Number", command=self.sort_number)

        self.root.configure(bg="#564D65")
        self.sort_name_button.pack(pady=10)
        self.sort_num_button.pack(pady=10)
        self.tree.pack(pady=10)

    def configure_headings(self):
        self.tree.heading("#0", text="Name")
        for col in ("Number", "Type", "Height", "Weight"):
            self.tree.heading(col, text=col)

    def import_csv(self):
        try:
            filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*csv")])
            with open(filename, "r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    name = row["Name"]
                    self.tree.insert("", tk.END, text=name, values=(row["Number"], row["Type"], row["Height"], row["Weight"]))
        except FileNotFoundError:
            messagebox.showerror("Error", "File Not Found")
        except Exception as e:
            messagebox.showerror("Error", e)

    def sort_name(self):
        sorted_monsters = sorted(self.get_values().items())
        self.update_tree_view(sorted_monsters)

    def sort_number(self):
        sorted_monsters = sorted(self.get_values().items(), key=lambda x: x[1]["Number"])
        self.update_tree_view(sorted_monsters)

    def get_values(self):
        all_data = {}
        for item in self.tree.get_children():
            name = self.tree.item(item, "text")
            all_values = self.tree.item(item, "values")

            data = {
                "Number": int(all_values[0]),
                "Type": all_values[1],
                "Height": all_values[2],
                "Weight": all_values[3]
            }

            all_data[name] = data
        return all_data
    
    def update_tree_view(self, sorted_monsters):
        self.tree.delete(*self.tree.get_children())
        for name, info in sorted_monsters:
            self.tree.insert("", "end", text=name, values=(info["Number"], info["Type"], info["Height"], info["Weight"]))

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    root.title("Monster Viewer")
    application = App(root, style)
    root.mainloop()
