import csv

class Rooms:
    def __init__(self):
        self.csv = csv
    def rooms(self, roomid):
        with open("rooms.csv", mode="r") as f:
            reader = self.csv.reader(f)
            for rows in reader:
                if rows[0] == roomid:
                    rooms = rows[1]
        return rooms
    def get_rooms(self):
        rooms = []
        with open("rooms.csv", mode="r") as f:
            reader = self.csv.reader(f)
            next(reader)
            for rows in reader:
                rooms.append(rows[1])
        return rooms
    def reverse_rooms(self, room):
        rooms = []
        with open("rooms.csv", mode="r") as f:
            reader = self.csv.reader(f)
            next(reader)
            for rows in reader:
                if rows[1] == room:
                    rooms = rows[0]
        return rooms