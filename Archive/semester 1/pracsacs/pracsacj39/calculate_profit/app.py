import tkinter as tk
from tkinter import messagebox
from get_profit import GetProfit

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.profit_get = GetProfit()

        self.get_profit_button = tk.Button(self.root, text="Get Profit", command=self.get_profit)
        self.profit_label = tk.Label(self.root)

        self.run()

    def get_profit(self):
        try:
            cul_price = self.profit_get.profit_get()
            self.profit_label.configure(text=cul_price)
        except Exception as e:
            messagebox.showerror("Error", f"Fatal Error: {e}")

    def run(self):
        self.get_profit_button.pack()
        self.profit_label.pack()
        self.root.mainloop()