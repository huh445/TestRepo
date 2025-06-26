from import_csv import ImportCSV

class App:
    def __init__(self):
        self.import_csv = ImportCSV()
        self.filename = self.validate_file()
        self.rows = self.csv_import()
        profit = 

    def validate_file(self):
        file = input("Enter the path to the file: ")
        if file.endswith(".csv"):
            print(f"Path Successful, {file}")
            return file
        else:
            print(f"That is not a CSV file")
    
    def csv_import(self):
        self.import_csv.import_csv(self.filename)
    
    def get_profit(self):
        for rows in self.rows:
            