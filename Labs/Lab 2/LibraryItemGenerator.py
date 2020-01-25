from DVD import DVD
from book import Book
from journal import Journal


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
            num_copies = int(input("Enter number of copies (positive number): "))
            item_data = (call_num, title, num_copies)

            # creates the item object of input choice
            if user_input == 1:
                author = input("Enter Author Name: ")
                return Book(item_data[0], item_data[1], item_data[2], author)
            if user_input == 2:
                release_date = input("Enter release date (yyyy/mm/dd): ")
                code = input("Enter region code: ")
                return DVD(item_data[0], item_data[1], item_data[2], release_date, code)
            if user_input == 3:
                names = input("Enter names")
                issue_number = input("Please enter issue number")
                publisher = input("Enter publisher")
                return Journal(item_data[0], item_data[1], item_data[2], names, issue_number, publisher)
            # return to menu
            if user_input == 4:
                pass






