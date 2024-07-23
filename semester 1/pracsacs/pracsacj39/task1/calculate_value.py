class CalculateValue:
    def __init__(self):
        pass
    def calculate_value(self, price, age):
        depreciation = price * 0.1 * age
        if depreciation > price:
            return 0
        else:
            return price - depreciation