""" user"""
from budget import Budget
from transactionRecords import TransactionRecords


class User:

    def __init__(self, budget, lockout_limit, warning_limit):
        self._budget = budget
        self._transaction_records = TransactionRecords()

        # replace with property in asn
        budget.get_lockout_limit = lockout_limit
        budget.get_warning_limit = warning_limit

    def add_transaction_record(self, time, amount, budget_cat, name):
        self._transaction_records.add_record(time, amount, budget_cat, name)

    def get_transaction_record(self):
        return self._transaction_records

