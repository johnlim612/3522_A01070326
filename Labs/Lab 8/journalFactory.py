from itemFactory import ItemFactory
from book import Book
from journal import Journal


class JournalFactory(ItemFactory):

    def create_item(self, call_num, title, num_copies):
        names = input("Enter names")
        issue_number = input("Please enter issue number")
        publisher = input("Enter publisher")
        return Journal(call_num, title, num_copies, names, issue_number, publisher)

