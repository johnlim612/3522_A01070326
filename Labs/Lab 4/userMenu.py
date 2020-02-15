""" User menu"""
from userHandler import UserCollection


class UserMenu:
    user_collection = UserCollection

    def __init__(self):
        self.run_menu()

    def run_menu(self):
        print("welcome to the user menu")
        self.user_collection.record_transaction()








