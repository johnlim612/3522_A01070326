from user import User


class TroubleMaker(User):
    def __init__(self):
        super().__init__()
        self._warning_limit = 0.75
        self._lockout_limit = 1.20
