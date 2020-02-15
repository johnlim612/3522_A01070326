""" Transaction Records"""


class TransactionRecords:
    def __init__(self):
        self._record_list = []

    def add_record(self, time, amount, budget_cat, name):
        record = [time, amount, budget_cat, name]
        self._record_list.append(record)

    def print_record(self):
        for x in self._record_list:
            print(x)
            for y in self._record_list[x]:
                print(y, ':', self._record_list[x][y])
