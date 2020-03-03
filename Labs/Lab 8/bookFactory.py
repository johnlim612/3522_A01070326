from itemFactory import ItemFactory
from book import Book


class BookFactory(ItemFactory):

    def create_item(self, call_num, title, num_copies):
        author = input("Enter Author Name: ")
        return Book(call_num, title, num_copies, author)

