import tkinter as tk
from pracsacj39.calculate_profit.get_profit import GetProfit

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.profit_get = GetProfit()

        self.get_profit_button = tk.Button(self.root, text="Get Profit", command=self.get_profit)
        self.profit_label = tk.Label(self.root)
        self.pack()

    def get_profit(self):
        cul_price = self.profit_get.profit_get()
        self.profit_label.configure(text=cul_price)
    def pack(self):
        self.get_profit_button.pack()
        self.profit_label.pack()
        self.root.mainloop()