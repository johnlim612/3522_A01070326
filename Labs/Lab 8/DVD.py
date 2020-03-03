""" This module holds DVD"""
from items import Items


class DVD(Items):
    """
    Represents a DVD in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, release_date, code):
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._code = code

    def __str__(self):
        return f"---- DVD: {self.title()} ----\n" \
            f"Call Number: {self.call_number}\n" \
            f"Number of Copies: {self._num_copies}\n" \
            f"Release Date: {self._release_date}" \
            f"Region Code: {self._code}"



