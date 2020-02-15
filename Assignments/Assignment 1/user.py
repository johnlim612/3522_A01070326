""" user"""
from budget import Budget
from transactionRecords import TransactionRecords
from userTypes import UserTypes

# from enum import Enum
#
# class userType(Enum):


class User:

    def __init__(self, name, age, bank_account_number, bank_name, bank_bal, budgets, user_type):
        self._name = name
        self._age = age
        self._bank_account_number = bank_account_number
        self._bank_name = bank_name
        self._bank_bal = bank_bal

        self._warning_limit = 0
        self._lockout_limit = 0

        self._budgets = budgets
        self._user_type = user_type
        self._user_types = UserTypes(user_type)

        self._transaction_records = TransactionRecords()
        self._budgets = Budget(budgets, self._user_types.warning_limit(), self._user_types.warning_limit())

    def add_transaction_record(self, time, amount, budget_cat, name):
        self._transaction_records.add_record(time, amount, budget_cat, name)

    def get_transaction_record(self):
        return self._transaction_records

    def notify_user(self, budget_cat):
        if self._budgets.check_notify(budget_cat):
            self._user_types.notify_user()

    def warn_user(self, budget_cat):
        if self._budgets.check_warning(budget_cat):
            self._user_types.notify_user()

    def get_budget(self):
        return self._budgets

    def get_bank_bal(self):
        return self._bank_bal

    def subtract_bank_bal(self, amount):
        self._bank_bal -= amount

    def check_warning(self, budget_cat):
        self._budgets.check_warning(budget_cat)

    def get_name(self):
        return self._name

    def view_budget(self):
        self._budgets.view_budget()

    def view_bank_details(self):
        print(f"Bank account Number: {self._bank_account_number}\n"
              f"Bank name: {self._bank_name}\n"
              f"Bank bal: {self._bank_bal}")


