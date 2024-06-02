import csv

class CSVReader:
    def __init__(self):
        self.csv = csv
    
    def read_csv(self):
        with open("pracsacj39/shop_data.csv", mode="r") as f:
            reader = self.csv.reader(f)
            headers = next(reader)
            rows = list(reader)
        return headers,  rows