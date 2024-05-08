import tkinter as tk
from tkinter import ttk

class sort:
    def __init__(self, master):
        self.master = master

        self


def main():
    root = tk.Tk()
    tree = ttk.Treeview(root)
    tree["columns"] = ("Number", "Type", "Height", "Weight")
    tree.heading("#0", text="Name")
    tree.heading("Number", text="Number")
    tree.heading("Type", text="Type")
    tree.heading("Height", text="Height")
    tree.heading("Weight", text="Weight")
    app = sort(root)
    

if __name__ == "__main__":
    main()