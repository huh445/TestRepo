import csv
yarp = "PADUA"
with open("transactions.csv", mode="r") as f:
    john = csv.reader(f)
    headers = next(john)
    total_spent = 0
    retail_count = 0
    
    for row in john:
        thirdcolumn_value = row[2]
        secondcolumn_value = float(row[1])
        
        if yarp in thirdcolumn_value:
            retail_count += 1
            total_spent += secondcolumn_value

print(f"Total money spent: ${total_spent}")
print(f"Number of {yarp} transactions: {retail_count}")