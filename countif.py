import csv
with open("C:\\transactions.csv", "r") as f:
    csvreader = csv.reader(f)
    steven = 0
    next(csvreader, None)
    third = []
    for row in csvreader:
        third.append(row[2])
        for john in third:
            john2 = john.strip().split()
        firstfour = john2[:10]
        if "RETAIL" in firstfour:
            steven += 1
    print(steven)