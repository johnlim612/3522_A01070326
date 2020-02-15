from user import User


class Rebel(User):
    def __init__(self):
        super().__init__()
        self._warning_limit = 0.50
        self._lockout_limit = 1.00

    def full_lockout(self):
        pass
