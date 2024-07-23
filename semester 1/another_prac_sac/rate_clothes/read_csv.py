import csv
class ImportCSV:
    def __init__(self):
        self.csv = csv
    def import_csv(self, file):
        with open(file, mode="r") as f:
            reader = self.csv.reader(f)
            data = list(reader)
        return data
    
    def add_file(self, list):
        with open("another_prac_sac/sales_data_new.csv", mode="w", newline=("")) as f:

            headers = list[0]

            writer = self.csv.DictWriter(f, fieldnames=headers)

            writer.writeheader()

            for row in list[1:]:
                if len(row) == len(headers):
                    writer.writerow(dict(zip(headers, row)))
                else:
                    pass