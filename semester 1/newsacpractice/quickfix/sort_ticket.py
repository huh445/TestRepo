class Sort:
    def __init__(self):
        pass
    def sort_ticket(self, rows, headers):
        sorted_ticket = sorted(rows, key=lambda x: int(x[0]))
        return sorted_ticket, headers
    def sort_search(self, rows, headers, key):
        sorted = []
        for row in rows:
            if row[2].lower() == key.lower():
                sorted.append(row)
        return sorted, headers