class Search:
    def __init__(self):
        pass
    def search(self, list, first_name, last_name, book_name):
        sorted_list = []
        for items in list:
            if book_name.lower() == items["book_name"].lower() and first_name.lower() == items["first_name"].lower() and last_name.lower() == items["last_name"].lower():
                sorted_dict = {"book_name": items["book_name"], "first_name": items["first_name"], "last_name": items["last_name"], "rating": items["rating"]}
                sorted_list.append(sorted_dict)
        return sorted_list