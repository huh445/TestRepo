import csv

class ImportRooms:
    def __init__(self):
        self.csv = csv
    def import_rooms(self, roomid):
        values = []
        with open("rooms.csv", mode="r") as f:
            reader = self.csv.reader(f)
        for row in reader:
            values.append(row[1])
        return values