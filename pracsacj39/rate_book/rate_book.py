import tkinter as tk
from tkinter import messagebox
class RateBook:
    def __init__(self):
        pass

    def get_rating(self, list, first_name, last_name):
        self.root = tk.Tk()
        self.list = list

        
        self.rating_label = tk.Label(self.root, text="Rating (1-5)")
        self.rating_entry = tk.Entry(self.root)

        self.get_rating_button = tk.Button(self.root, text="Rate", command=self.rate_book)

        self.run()
        
    def rate_book(self):
        rating = self.rating_entry.get()
        if int(rating) > 5 or int(rating) < 0:
            messagebox.showerror("Error", "Rating can only be 1-5")
            self.root.destroy()
            return
        else:
            self.list["rating"] = rating
        return rating

    def run(self):
        self.rating_label.pack()
        self.rating_entry.pack()

        self.get_rating_button.pack()

        self.root.mainloop()