import csv
import tkinter as tk
from tkinter import ttk
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
from PIL import Image, ImageTk
from io import BytesIO
from collections import defaultdict

class App:
    def __init__(self, root, tree):
        self.root = root
        self.tree = tree
        self.check = tk.Button(self.root, text="Check transactions", command=self.compare)
        self.allCheck = tk.Button(self.root, text="Check all spent", command=self.all)
        self.entry = tk.Entry(self.root)
        self.info = tk.Label(self.root)
        self.count = 0
        self.spent = 0
        self.rows = []
        self.balance = defaultdict(float)
        self.count_by_date = defaultdict(int)
        
        self.canvas = tk.Label(self.root)
        
        self.pack()

    def importcsv(self):
        with open("transactions.csv", mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            self.tree["columns"] = headers

            for header in headers:
                self.tree.heading(header, text=header)
                self.tree.column(header)

            for row in reader:
                self.rows.append(row)
                self.tree.insert("", tk.END, values=row)

    def compare(self):
        keyword = self.entry.get().upper()
        self.count = 0
        self.spent = 0

        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in self.rows:
            transactions = row[2].upper()
            value = float(row[1])
            if keyword in transactions:
                self.count += 1
                self.spent += value
                self.tree.insert("", tk.END, values=row)

                self.count_by_date[row[0]] += 1

        self.info.config(text=f"Amount spent: ${self.spent:.2f} Amount of transactions: {self.count}")

        self.plotGraph(keyword)
    def all(self):
        keyword = ""
        self.count = 0
        self.spent = 0
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in self.rows:
            transactions = row[2].upper()
            value = float(row[1])
            if value < 0:
                self.count += 1
                self.spent += value
                self.tree.insert("", tk.END, values=row)

                self.count_by_date[row[0]] += 1
        
        self.info.config(text=f"Amount spent: ${self.spent:.2f} Amount of transactions: {self.count}")

        self.plotGraph(keyword)

    def plotGraph(self, keyword=None):
        self.balance.clear()
        cumulative_spent = 0
        dates = []

        for row in self.rows:
            date = row[0]
            amount = float(row[1])
            transaction = row[2].upper()
            if keyword is None or keyword in transaction:
                cumulative_spent += amount
                self.balance[date] = cumulative_spent
                dates.append(date)

        cumulative_spent_values = [self.balance[date] for date in dates]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=np.arange(1, len(dates) + 1), y=cumulative_spent_values, mode='lines+markers', name='Cumulative Spent'), secondary_y=False)
        fig.update_layout(title='Cumulative Spent and Count of Transactions Over Time', xaxis_title='Transaction Number', yaxis_title='Cumulative Spent')

        img_bytes = fig.to_image(format="png")
        img = Image.open(BytesIO(img_bytes))
        img = img.resize((800, 600), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)

        self.canvas.config(image=img_tk)
        self.canvas.image = img_tk

    def pack(self):
        self.root.title("Financial Analyser")
        self.importcsv()
        self.info.pack()
        self.info.config(font=("Arial", 24))
        self.entry.pack()
        self.check.pack()
        self.allCheck.pack()
        self.tree.pack(expand=True, fill='both')
        self.canvas.pack()
        self.plotGraph()

if __name__ == "__main__":
    root = tk.Tk()
    tree = ttk.Treeview(root)
    app = App(root, tree)
    root.mainloop()
