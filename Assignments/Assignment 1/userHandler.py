""" This module houses the Catalogue"""
import datetime
from userTypeEnum import UserType
from user import User


class UserCollection:
    user_list = []


    def add_user(self, user):
        self.user_list.append(user)

    # @staticmethod
    # def load_test_user():
    #     budget = Budget(200, 300, 250, 100)
    #     # Dummy troublemaker user type values
    #     user = User()
    #     return user

    @staticmethod
    def record_transaction(self, user):
        amount = input("Please enter you transaction amount")

        time = datetime.datetime.now().time()
        name = user.get_name()
        option = int(input("Which budget category is your transaction in? (input number)"
                           "\n1-Games and Entertainment"
                           "\n2-Clothing and Accessories"
                           "\n3-eating out"
                           "\n4-Miscellaneous"))
        if option == 1:
            budget_cat = "games and entertainment"
        elif option == 2:
            budget_cat = "clothing and accessories"
        elif option == 3:
            budget_cat = "eating out"
        elif option == 4:
            budget_cat = "miscellaneous"
        else:
            budget_cat = "none"

        users_budget = user.get_budget

        if user.get_bank_bal() - amount < 0:
            print("You dont't have enough money in the bank")
            return
        # adds transaction record after checking it is not locked
        budget_lock = user.get_budget.get_locked()
        user.warn_user(budget_cat)
        user.notify_user(budget_cat)

        if not budget_lock.get(budget_cat):
            user.add_transaction_record(time, amount, budget_cat, name)
        # subtracts amount from budget if not locked, and locks if surpasses budget after transaction
        users_budget.subtract_budget(amount, budget_cat)
        user.subtract_bank_bal(amount)

        # prints list of records
        user.get_transaction_record().print_record()

    def register_child(self):

        registered_budget = False
        games_entertainment = 0
        clothing_accessories = 0
        eating_out = 0
        misc = 0
        print("Please register your child")
        name = input("What is their name?")
        age = input("Enter age")
        bank_account_num = input("Enter bank account number")
        bank_name = input("Enter bank name")
        bank_bal = input("Enter bank balance")

        while not registered_budget:
            try:
                print("Enter Budget for each category:")
                games_entertainment = float(input("Games and Entertainment: "))
                clothing_accessories = float(input("Clothing and Accessories: "))
                eating_out = float(input("Eating Out: "))
                misc = float(input("Miscellaneous: "))

                registered_budget = True

            except AttributeError:
                print("You have entered an invalid number")

        input_budgets = {"games and entertainment": games_entertainment,
                         "clothing and accessories": clothing_accessories,
                         "eating out": eating_out,
                         "miscellaneous": misc}

        user_type = 0
        while user_type not in (1, 2, 3):
            user_type = int(input("Enter the user type:"
                                  "\n1- Angel"
                                  "\n2- Troublemaker"
                                  "\n3- Rebel"))
            if user_type == 1:
                user_type = UserType.Angel
            elif user_type == 2:
                user_type = UserType.TroubleMaker
            elif user_type == 3:
                user_type = UserType.Rebel
            else:
                print("Please enter one of the options")

        user = User(name, age, bank_account_num, bank_name, bank_bal, input_budgets, user_type)
        self.add_user(user)


