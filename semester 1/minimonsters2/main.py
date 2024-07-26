import tkinter as tk
from tkinter import ttk
from app import App

if __name__ == "__main__":
    root = tk.Tk()
    tree = ttk.Treeview(root)
    app = App(root, tree)
    root.mainloop()