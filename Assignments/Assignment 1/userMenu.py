""" User menu"""
from userHandler import UserCollection
from user import User


class UserMenu:

    def __init__(self):
        self._user_handler = UserCollection()

    def start(self):
        self._user_handler.register_child()
        user = self._user_handler.user_list[-1]
        a = True
        print("Showing user menu for child...")
        choice = 0
        while a:
            choice = int(input("What would you like to do?"
                               "\n1- View Budgets"
                               "\n2- Record a Transaction"
                               "\n3- View Transactions By Budget"
                               "\n4- View Bank Account Details"))

            if choice == 1:
                user.view_budget()
                print("worked")
            elif choice == 2:
                self._user_handler.record_transaction(user)
            elif choice == 3:
                print(user.get_transaction_record())
            elif choice == 4:
                user.view_bank_details()
            else:
                print("Please enter a valid option")
