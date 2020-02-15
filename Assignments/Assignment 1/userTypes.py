class UserTypes:
    def __init__(self, user_type):
        self._lockout_limit = self.lockout_limit()
        self._warning_limit = self.warning_limit()
        self._user_type = user_type
        self._warned = 0

    def lockout_limit(self):
        if self._user_type == 1:
            return 'inf'
        if self._user_type == 2:
            return 1.20
        if self._user_type == 3:
            return 1.00

    def warning_limit(self):
        if self._user_type == 1:
            return 0.90
        if self._user_type == 2:
            return 0.75
        if self._user_type == 3:
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




