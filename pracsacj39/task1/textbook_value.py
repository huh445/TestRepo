import tkinter as tk
from tkinter import messagebox
from calculate_value import CalculateValue

class TextbookValue:
    def __init__(self):
        self.root = tk.Tk()
        self.calculate_value = CalculateValue()

        self.age_label = tk.Label(self.root, text="How old is the textbook (in years)?")
        self.age_entry = tk.Entry(self.root)
        self.price_label = tk.Label(self.root, text="How much did you pay for the textbook?")
        self.price_entry = tk.Entry(self.root)
        self.get_price = tk.Button(self.root, text="Calculate Current value of the textbook", command=self.user_input)

        self.run()

    def user_input(self):
        age = int(self.age_entry.get())
        price = int(self.price_entry.get())
        price = self.calculate_value.calculate_value(price, age)
        messagebox.showinfo("Price", f"The price is {price}")
        
    def run(self):
        self.age_label.pack()
        self.age_entry.pack()
        self.price_label.pack()
        self.price_entry.pack()
        self.get_price.pack()
        self.root.mainloop()