import csv
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict

class App:
    def __init__(self, root, tree, canvas):
        self.root = root
        self.tree = tree
        self.canvas = canvas
        self.check = tk.Button(self.root, text="Check transactions", command=self.onEnterPressed)
        self.entry = tk.Entry(self.root)
        self.entry.bind("<Return>", self.onEnterPressed)
        self.info = tk.Label(self.root)
        self.rows = []  # Store rows for later use
        self.balance = defaultdict(float)  # Store cumulative balance for each date
        self.countByDate = defaultdict(int)  # Store count of transactions for each date
        self.pack()

    def importcsv(self):
        with open("transactions.csv", mode="r") as f:
            reader = csv.reader(f)
            headers = next(reader)
            self.tree["columns"] = headers

            for header in headers:
                self.tree.heading(header, text=header)
                self.tree.column(header)

            for row in reader:
                self.rows.append(row)  # Store each row
                self.tree.insert("", tk.END, values=row)
    def onEnterPressed(self, keyword=None):
        keyword = self.entry.get().upper()
        if keyword:
            self.compare()
        else:
            self.all()

    def compare(self, keyword=None):
        keyword = self.entry.get().upper()  # Convert to uppercase for case-insensitive comparison
        count = 0
        spent = 0

        # Clear the current Treeview items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Filter and display transactions in the Treeview
        for row in self.rows:
            transactions = row[2].upper()  # Convert to uppercase for case-insensitive comparison
            value = float(row[1])
            if keyword in transactions:
                count += 1
                spent += value
                self.tree.insert("", tk.END, values=row)

                # Update count of transactions for the date
                self.countByDate[row[0]] += 1

        self.info.config(text=f"Amount spent: ${spent:.2f} Amount of transactions: {count}")

        # Plot graph with filtered data
        self.plotGraph(keyword)

    def all(self):
        self.canvas.get_tk_widget().pack_forget()
        count = 0
        spent = 0
        for item  in self.tree.get_children():
            self.tree.delete(item)
        for row in self.rows:
            value = float(row[1])
            if value < 0:
                count += 1
                spent += value
                self.tree.insert("", tk.END, values=row)
                self.countByDate[row[0]] += 1
        
        self.info.config(text=f"Toal spent: ${spent:.2f} Amount of negative transactions: {count}")

    def plotGraph(self, keyword=None):
        self.balance.clear()  # Clear previous balance data
        cumulative_spent = 0  # Initialize cumulative spent amount
        dates = []  # Initialize list to store dates

        for row in self.rows:
            date = row[0]
            amount = float(row[1])
            transaction = row[2].upper()
            if keyword is None or keyword in transaction:
                cumulative_spent += amount  # Update cumulative spent amount
                self.balance[date] = cumulative_spent  # Store cumulative spent amount for the date
                dates.append(date)  # Store the date

        cumulative_spent_values = [self.balance[date] for date in dates]

        fig, ax1 = plt.subplots(figsize=(8, 6))

        # Plot cumulative spent amount
        ax1.plot(range(1, len(dates) + 1), cumulative_spent_values, color='tab:blue', marker='o', linestyle='-', label='Cumulative Spent')
        ax1.set_xlabel('Transaction Number')
        ax1.set_ylabel('Cumulative Spent', color='tab:blue')

        plt.title('Cumulative Spent and Count of Transactions Over Time')
        plt.xticks(range(1, len(dates) + 1), dates, rotation=45, ha='right')
        plt.tight_layout()

        # Show legend
        fig.legend(loc='upper left', bbox_to_anchor=(0.12,0.9))

        # Clear the existing canvas and draw the new graph
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=True, fill='both')


    def pack(self):
        self.root.title("Financial Analyser")
        self.importcsv()
        self.info.pack()
        self.info.config(font=("Arial", 24))
        self.entry.pack()
        self.check.pack()
        self.tree.pack(expand=True, fill='both')
        self.all()

if __name__ == "__main__":
    root = tk.Tk()
    tree = ttk.Treeview(root)
    canvas = FigureCanvasTkAgg(plt.figure(figsize=(8, 6)), master=root)
    app = App(root, tree, canvas)
    root.mainloop()