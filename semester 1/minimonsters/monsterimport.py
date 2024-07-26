import csv
class Search:
    def __init__(self):
        self.rows = []
        self.csv = csv
    def import_csv(self, filename):
        with open(filename, mode="r") as f:
            reader = self.csv.reader(f)
            headers = next(reader)
            rows = list(reader)
        self.rows = rows
        self.headers = headers
        return headers, rows
    def sort_name(self):
        sortedMonster = sorted(self.rows, key=lambda x: x[0])
        return sortedMonster, self.headers
    def sort_number(self):
        sortedMonster = sorted(self.rows, key=lambda x: int(x[1]))
        return sortedMonster, self.headers
    def sort_entry(self, key):
        sortedMonster = []
        for row in self.rows:
            if key in row:
                sortedMonster.append(row)
        return sortedMonster, self.headers