import csv

class ImportRooms:
    def __init__(self):
        self.csv = csv
    def import_rooms(self, roomid):
        with open("rooms.csv", mode="r") as f:
            reader = self.csv.reader(f)
            for rows in reader:
                if roomid == rows[0]:
                    values = rows[1]
        return values
    def all_rooms(self):
        rooms = []
        with open("rooms.csv", mode="r") as f:
            reader = self.csv.reader(f)
            for rows in reader:
                rooms.append(rows[1])
        return rooms
    def get_id(self, rooms):
        with open("rooms.csv", mode="r") as f:
            reader =self.csv.reader(f)
            for rows in reader:
                if rooms in rows[1]:
                    room = rows[0]
        return room