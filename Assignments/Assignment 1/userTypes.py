from userTypeEnum import UserType


class UserTypes:
    def __init__(self, user_type):
        self._lockout_limit = self.lockout_limit(user_type)
        self._warning_limit = self.warning_limit(user_type)
        self._user_type = user_type
        self._warned = 0

    def lockout_limit(self, user_type):
        if user_type == UserType.Angel:
            return 'inf'
        if user_type == UserType.TroubleMaker:
            return 1.20
        if user_type == UserType.Rebel:
            return 1.00

    def warning_limit(self, user_type):
        if user_type == UserType.Angel:
            return 0.90
        if user_type == UserType.TroubleMaker:
            return 0.75
        if user_type == UserType.Rebel:
            return 0.50

    def notify_user(self):
        warning_percentage = int(self._warning_limit * 100)
        if self._warned < 2:
            if self._user_type == 1:
                print(f"You have exceeded {warning_percentage}% on this budget category.")
                self._warned += 1
            if self._user_type == 2:
                print(f"You have exceeded {warning_percentage}% on this budget category.")
                self._warned += 1
        if self._user_type == 3:
            print(f"YOU HAVE EXCEEDED {warning_percentage}% ON THIS CATEGORY")

    def get_lockout_limit(self):
        return self._lockout_limit

    def get_warning_limit(self):
        return self._warning_limit
