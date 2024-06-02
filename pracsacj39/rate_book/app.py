import tkinter as tk
from tkinter import ttk, messagebox
from read_csv import ReadCSV
from search import Search

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.csv_read = ReadCSV()
        self.search = Search()

        self.tree = ttk.Treeview(self.root)
        
        self.first_name_label = tk.Label(self.root, text="First Name:")
        self.first_name_entry = tk.Entry(self.root)

        self.last_name_label = tk.Label(self.root, text="Last Name:")
        self.last_name_entry = tk.Entry(self.root)

        self.book_label = tk.Label(self.root, text="Book Name:")
        self.book_entry = tk.Entry(self.root)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_list)

        self.rate_book_label = tk.Label(self.root, text="Rate the book (1/5)")
        self.rate_book_entry = tk.Entry(self.root)
        self.rate_book_button = tk.Button(self.root, text="Rate the book", command=self.rate_book)
        
        self.init_tree()
        self.run()

    def init_tree(self):
        self.list = self.read_csv()
        self.list_const = self.list
        self.tree.heading("#0", text="Book Name")
        self.tree["columns"] = ("first_name", "last_name")
        self.tree.heading("first_name", text="First Name", anchor=tk.W)
        self.tree.heading("last_name", text="Last Name", anchor=tk.W)
        self.update_tree(self.list)

    def read_csv(self):
        return self.csv_read.read_csv()
    
    def rate_book(self):
        rating = self.rate_book_entry.get()
        if int(rating) < 0 or int(rating) > 5:
            messagebox.showerror("Error", "Rating has to be from 1 to 5.")
            return
        index = self.list_const.index(self.list[0])
        del self.list_const[index]
        self.list[0]["rating"] = rating
        self.list_const.insert(index, self.list[0])
        self.csv_read.create_csv(self.list_const)

    
    def search_list(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        book_name = self.book_entry.get()
        self.first_name, self.last_name = first_name, last_name
        self.list = self.search.search(self.list, first_name, last_name, book_name)
        self.update_tree(self.list)
        self.rate_book_label.pack()
        self.rate_book_entry.pack()
        self.rate_book_button.pack()
    
    def update_tree(self, list):
        self.tree.delete(*self.tree.get_children())
        for info in list:
            book_name = info["book_name"]
            first_name = info["first_name"]
            last_name = info["last_name"]
            
            self.tree.insert("", tk.END, text=book_name, values=(first_name, last_name))

    def run(self):
        self.first_name_label.pack()
        self.first_name_entry.pack()
        
        self.last_name_label.pack()
        self.last_name_entry.pack()

        self.book_label.pack()
        self.book_entry.pack()

        self.search_button.pack()

        self.tree.pack()

        self.root.mainloop()