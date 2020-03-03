
from abc import ABC
"""
    Represents a single item in a library which is identified through
    it's call number.
    """


class Items(ABC):
    """ Item constructor"""
    def __init__(self, call_num, title, num_copies):
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies

    def get_title(self):
        return self._title.title()

    def increment_number_of_copies(self):
        self._num_copies += 1

    def decrement_number_of_copies(self):
        self._num_copies -= 1

    def get_num_copies(self):
        return self._num_copies

    # property for number of copies
    num_copies = property(get_num_copies)

    # property for item title
    title = property(get_title)

    @property
    def call_number(self):
        return self._call_num

    def check_availability(self):
        if self._num_copies > 0:
            return True
        else:
            return False

