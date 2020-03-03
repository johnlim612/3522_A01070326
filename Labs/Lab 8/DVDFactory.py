from itemFactory import ItemFactory
from DVD import DVD


class DVDFactory(ItemFactory):

    def create_item(self, call_num, title, num_copies):
        release_date = input("Enter release date (yyyy/mm/dd): ")
        code = input("Enter region code: ")
        return DVD(call_num, title, num_copies, release_date, code)
