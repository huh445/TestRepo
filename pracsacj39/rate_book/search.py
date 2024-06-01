class Search:
    def __init__(self):
        pass
    def search(self, list, first_name, last_name, book_name):
        sorted_list = []
        for items in list:
            if book_name == items["book_name"] and first_name == items["first_name"] and last_name== items["last_name"]:
                sorted_dict = {"book_name": items["book_name"], "first_name": items["first_name"], "last_name": items["last_name"]}
                sorted_list.append(sorted_dict)
        return sorted_list