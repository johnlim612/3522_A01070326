""" This module houses the Catalogue"""
from LibraryItemGenerator import LibraryItemGenerator
import difflib


class Catalogue:
    """
    Represents a catalogue in a library used to search, add, remove items. Holds
    a list of all items.
    """

    def __init__(self, item_list):
        """
        Intialize the library with a list of .
        :param item_list: a sequence of item objects.
        """
        self._item_list = item_list

    def find_items(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for items in self._item_list:
            title_list.append(items.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new item to the library with a unique call number.
        """
        call_number = input("Enter call number")
        generator = LibraryItemGenerator()
        new_item = generator.generate_item(call_number)
        found_item = self.retrieve_item_by_call_number(call_number)
        if found_item:
            print(f"Could not add item with call number "
                  f"{call_number}. It already exists. ")
        else:
            self._item_list.append(new_item)
            print("item added successfully! item details:")
            print(new_item)

    def remove_item(self, call_number):
        """
        Remove an existing item from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self.retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("Item List")
        print("--------------", end="\n\n")
        for library_item in self._item_list:
            print(library_item)

    def retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: item object if found, None otherwise
        """
        found_item = None
        for library_item in self._item_list:
            if library_item.call_number == call_number:
                found_item = library_item
                break
        return found_item

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count decremented, false
        otherwise.
        """
        library_item = self.retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_number):
        """
        Increment the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        library_item = self.retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False
