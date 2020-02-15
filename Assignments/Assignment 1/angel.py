from user import User


class Angel(User):
    def __init__(self):
        super().__init__()
        self._warning_limit = 0.90
        self._lockout_limit = float('inf')
