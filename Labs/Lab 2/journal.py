""" This module holds DVD"""
from items import Items
import difflib


class Journal(Items):

    def __init__(self, call_num, title, num_copies, names, number, publisher):
        super().__init__(call_num, title, num_copies)
        self._names = names
        self._number = number
        self._publisher = publisher

    def __str__(self):
        return f"---- Journal: {self.get_title()} ----\n" \
            f"Call Number: {self.call_number}\n" \
            f"Number of Copies: {self._num_copies}\n" \
            f"names: {self._names}\n" \
            f"Issue Number: {self._number}\n" \
            f"Issue Number: {self._publisher}\n" \



