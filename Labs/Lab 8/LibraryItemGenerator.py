from DVD import DVD
from book import Book
from journal import Journal
from bookFactory import BookFactory
from DVDFactory import DVDFactory
from journalFactory import JournalFactory


class LibraryItemGenerator:
    """
    Generates and returns an item of input choice
        """
    @staticmethod
    def generate_item(call_num):
        user_input = None
        # If entered invalid option, loops user back to choices below
        while user_input != 4:
            print("What type of item would you like to add")
            print("1. Book")
            print("2. DVD")
            print("3. Journal")
            print("4. Back")
            string_input = input("Please enter your choice (1-4)")
            user_input = int(string_input)
            title = input("Enter title: ")

            wrong_input = True
            while wrong_input:
                try:
                    num_copies = int(input("Enter number of copies (positive number): "))
                    wrong_input = False
                except ValueError:
                    print("please enter a valid input")

            # creates the item object of input choice
            if user_input == 1:

                return BookFactory().create_item(call_num, title, num_copies)
            if user_input == 2:
                return DVDFactory().create_item(call_num, title, num_copies)
            if user_input == 3:
                return JournalFactory().create_item(call_num, title, num_copies)
            # return to menu
            if user_input == 4:
                pass






