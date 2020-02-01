""" Transaction Records"""


class TransactionRecords:
    def __init__(self):

        self._record_list = []

    def add_record(self, time, amount, budget_cat, name):
        record = [time, amount, budget_cat, name]
        self._record_list.insert(record)

    def print_record(self):
        print(self._record_list)
