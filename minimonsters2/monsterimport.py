import csv

class Search:
    def __init__(self, filename):
        self.rows = []
        self.csv = csv
        self.filename = filename
    def import_csv(self):
        with open(self.filename, mode="r") as f:
            reader = self.csv.reader(f)
            headers = next(reader)
            rows = list(reader)
        print(rows)
        self.rows = rows
        self.headers = headers
        return headers, rows
    def search_filter(self, key):
        sortedMonster = []
        for row in self.rows:
            if key in row:
                sortedMonster.append(row)
        return self.headers, sortedMonster
    def sort_alpha(self):
        sortedMonster = sorted(self.rows, key=lambda x: x[0])
        return self.headers, sortedMonster
    def sort_num(self):
        sortedMonster = sorted(self.rows, key=lambda x: int(x[1]))
        return self.headers, sortedMonster
    
    def add_data(self, data):
        with open(self.filename, mode="a", newline="") as f:
            writer = self.csv.writer(f)
            writer.writerow(data)
            self.import_csv()

    def highest_monster(self):
        john, rows = self.import_csv()
        for row in rows:
            max_id = row[1]
        return int(max_id)