import csv

class ReadCSV:
    def __init__(self):
        self.csv = csv
    def read_csv(self):
        info = []
        with open("pracsacj39/shop_data.csv", mode="r") as f:
            reader = self.csv.reader(f)
            headers = next(reader)
            for row in reader:
                book_name = row[0]
                name = row[4]
                rating = row[6]
                if "NA" not in name:
                    first_name, last_name = name.split(" ", 1)
                    info_dict = {"book_name": book_name, "first_name": first_name, "last_name": last_name, "rating": rating}
                    info.append(info_dict)
        return info
    
    def create_csv(self, list):
        with open("pracsacj39/shop_data_new.csv", mode="w", newline=("")) as f:
            column_names = list[0].keys()

            writer = self.csv.DictWriter(f, fieldnames=column_names)

            writer.writeheader()

            for data in list:
                writer.writerow(data)