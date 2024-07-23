class Sort:
    def __init__(self):
        pass
    # def sort_subject(self, rows):
    #     sorted_subject = sorted(rows, key=lambda x: x[1])
    #     return sorted_subject
    # def sort_textbook(self, rows):
    #     sorted_textbook = sorted(rows, key=lambda x: x[0])
    #     return sorted_textbook
    def sort_rating(self, rows):
        sorted_rating = sorted(rows, key=lambda x: x[6])
        return sorted_rating