""" Holds a the budget object for each user"""


class Budget:

    def __init__(self, budgets, lockout_limit, warning_limit):
        self._budgets = budgets
        self._current_budgets = budgets
        self._warning_limit = warning_limit
        self._lockout_limit = lockout_limit
        self._locked = {"games and entertainment": False,
                        "clothing and accessories": False,
                        "eating out": False,
                        "miscellaneous": False}

    def check_lockout(self, budget_cat):
        # percentage of budget used
        used_percentage = (self._budgets[budget_cat] - self._current_budgets[budget_cat]) / self._budgets[budget_cat]
        if used_percentage > self._lockout_limit:
            self.lock_budget(budget_cat)

    def get_lockout_limit(self):
        return self._lockout_limit

    def get_warning_limit(self):
        return self._warning_limit

    def get_current_budget(self):
        return self._current_budgets

    def get_locked(self):
        return self._locked

    def lock_budget(self, budget_cat):
        self._locked[budget_cat] = True
        print(f"You have exceeded your limit for {budget_cat} and have been locked")

    # budget_cat is string
    def subtract_budget(self, amount, budget_cat):

        if self._locked.get(budget_cat):
            print("You are locked out from this budget category")
            return
        self._current_budgets[budget_cat] -= amount
        # subtract from transactions

    def check_warning(self, budget_cat):
        # percentage of budget used
        used_percentage = (self._budgets[budget_cat] - self._current_budgets[budget_cat]) / self._budgets[budget_cat]

        if used_percentage > self._warning_limit:
            return True
        return False

    def check_notify(self, budget_cat):
        if self._budgets[budget_cat] <= 0:
            return True
        return False

    def view_budget(self):
        print("\n")
        for key, value in self._current_budgets.items():
            print(key, ": $", value)
        print("\n")
