import csv
class ImportCSV:
    def __init__(self):
        self.csv = csv
    def import_csv(self, file):
        profit = 0
        with open(file, mode="r") as f:
            reader = self.csv.reader(f)
            headers = next(reader)
            for rows in reader:
                if not rows[3] == "NA" and not rows[5] == "NA":
                    try:
                        purchase_price = int(rows[3])
                        sale_price = int(rows[5])
                        profit = profit + sale_price - purchase_price
                    except ValueError:
                        return "error"
                else:
                    pass
        return profit