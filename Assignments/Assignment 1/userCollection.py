""" This module houses the Catalogue"""
from user import User
from budget import Budget


class UserCollection:
    user_list = []

    def __init__(self):
        pass

    def register_user(self, user):
        pass

    @staticmethod
    def load_test_user():
        budget = Budget(200, 300, 250, 100)
        # Dummy troublemaker user type values
        user = User(budget, 120, 75)
        return user

    def record_transaction(self, user):
        time, amount, budget_cat, name = input("Please enter you transaction details "
                                               "(time amount budget-category name): ")
        user = self.load_test_user()
        user.add_transaction_record(time, amount, budget_cat, name)
        user.get_transaction_record().print_record()





