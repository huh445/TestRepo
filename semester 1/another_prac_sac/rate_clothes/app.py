import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from read_csv import ImportCSV
from search import Search
from add_rating import AddRating
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.import_csv = ImportCSV()
        self.search = Search()
        self.submit_rating = AddRating()
        
        self.clothing_name_entry = tk.Entry(self.root)
        self.first_name_entry = tk.Entry(self.root)

        self.clothing_name_label = tk.Label(self.root, text="Enter the clothing name item:")
        self.first_name_label = tk.Label(self.root, text="Enter your first name:")

        self.search_button = tk.Button(self.root, text="Search for name", command=self.search_data)

        self.rating_combo = ttk.Combobox(self.root, values=[1, 2, 3, 4, 5])
        self.submit_rating_button = tk.Button(self.root, text="Get Rating", command=self.add_rating)

        self.open_csv()
        self.run()

    def open_csv(self):
        file = filedialog.askopenfilename(title="Open CSV file", filetypes=[("CSV files", "*.csv")])
        if file:
            if file.endswith(".csv"):
                self.data = self.import_csv.import_csv(file)
            else:
                messagebox.showerror("Error", "Please make sure that you select a CSV file")
        else:
            messagebox.showerror("Error", "Please make sure that you select a file")
    
    def search_data(self):
        clothing_name = self.clothing_name_entry.get()
        first_name = self.first_name_entry.get()
        self.purchase = self.search.search(self.data, clothing_name, first_name)
        if not self.purchase == None:
            messagebox.showinfo("User", f"Purchase found.")
            self.rating_combo.pack()
            self.submit_rating_button.pack()
        else:
            messagebox.showerror("User", "Purchase not found. Make sure you inputted the right name.")
        
    def add_rating(self):
        rating = self.rating_combo.get()
        self.submit_rating.add_rating(rating, self.data, self.purchase)
    
    def run(self):
        self.clothing_name_label.pack()
        self.clothing_name_entry.pack()
        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.search_button.pack()
        self.root.mainloop()