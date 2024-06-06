class Search:
    def __init__(self):
        pass
    def search(self, data, clothing, name):
        for rows in data:
            if clothing.lower() == rows[0].lower() and name.lower() == rows[4].lower():
                return rows
        return None