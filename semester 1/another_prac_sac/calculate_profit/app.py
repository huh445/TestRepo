import tkinter as tk
from tkinter import messagebox, filedialog
from import_csv import ImportCSV
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.import_csv = ImportCSV()
        
        self.calculate_profit_button = tk.Button(self.root, text="Calculate Profit", command=self.calculate_profit)

        self.run()

    def calculate_profit(self):
        file = filedialog.askopenfilename(title="Open CSV files", filetypes=[("CSV Files", "*.csv")])
        if file:
            if file.endswith(".csv"):
                value = self.import_csv.import_csv(file)
                if value == "error":
                    messagebox.showerror("Warning", "Value Error")
                else:
                    messagebox.showinfo("Value", f"The total profit is {value}")
            else:
                messagebox.showerror("Warning", "You did not select a CSV file")
        else:
            messagebox.showerror("Warning", "You did not select a file.")
    
    def run(self):
        self.calculate_profit_button.pack()
        self.root.mainloop()