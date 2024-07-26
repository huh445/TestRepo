import tkinter as tk
from tkinter import ttk, messagebox
from csv_reader import CSVReader
from sort import Sort

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.csv = CSVReader()
        self.sort = Sort()
        self.tree = ttk.Treeview(self.root)
        self.sort_subject_button = tk.Button(self.root, text="Sort by Subject", command=self.sort_subject)
        self.sort_textbook_button = tk.Button(self.root, text="Sort by Textbook", command=self.sort_textbook)
        self.sort_rating_button = tk.Button(self.root, text="Sort by Rating", command=self.sort_rating)
        self.quit_button = tk.Button(self.root, text="Quit", command=lambda: self.root.destroy())
        self.import_tree()
        self.run()

    def import_tree(self):
        try:
            headers, rows = self.csv.read_csv()
            self.headers, self.rows = headers, rows
            self.tree["columns"] = headers
            self.update_tree(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Fatal error importing CSV:{e}")

    def sort_subject(self):
        try:
            rows = self.sort.sort_subject(self.rows)
            self.update_tree(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Fatal error sorting for subject: {e}")
    
    def sort_textbook(self):
        try:
            rows = self.sort.sort_textbook(self.rows)
            self.update_tree(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Fatal error sorting for textbook: {e}0")
    
    def sort_rating(self):
        try:
            rows = self.sort.sort_rating(self.rows)
            self.update_tree(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Fatal error sorting for rating: {e}")

    def update_tree(self, rows):
        try:
            self.tree.delete(*self.tree.get_children())
            for header in self.headers:
                self.tree.heading(header, text=header)
                self.tree.column(header)
            for row in rows:
                self.tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Fatal error updating tree: {e}")

    def run(self):
        self.tree.pack()
        self.sort_subject_button.pack()
        self.sort_textbook_button.pack()
        self.sort_rating_button.pack()
        self.quit_button.pack()
        self.root.mainloop()