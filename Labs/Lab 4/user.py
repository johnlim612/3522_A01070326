""" user"""
from budget import Budget
from transactionRecords import TransactionRecords


class User:

    def __init__(self, budget, lockout_limit, warning_limit):
        self._budget = budget
        self._transaction_record = TransactionRecords()

        # replace with property in asn
        budget.get_lockout_limit = lockout_limit
        budget.get_warning_limit = warning_limit


