from read_csv import ImportCSV
class AddRating:
    def __init__(self):
        self.csv = ImportCSV()

    def add_rating(self, rating, data, purchase):
        print(purchase)
        index = data.index(purchase)
        del data[index]
        purchase[6] = rating
        data.insert(index, purchase)
        self.csv.add_file(data)