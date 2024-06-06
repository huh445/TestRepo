import csv

class GetProfit:
    def __init__(self):
        self.csv = csv
    def profit_get(self):
        cul_price = 0
        with open("pracsacj39/calculate_profit/shop_data.csv", mode="r") as f:
            reader = self.csv.reader(f)
            header = next(reader)
            for rows in reader:
                purchase_price = rows[3]
                sale_price = rows[5]
                if sale_price == "NA":
                    purchase_price = purchase_price*-1
                else:
                    cul_price = cul_price + float(sale_price) - float(purchase_price)
        return cul_price