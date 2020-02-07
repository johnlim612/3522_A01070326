""" budget"""


class Budget:

    def __init__(self, games_entertainment, clothing, eating, misc):

        self._games_entertainment = games_entertainment
        self._clothing = clothing
        self._eating = eating
        self._misc = misc
        self._lockout_limit = 0
        self._warning_limit = 0

    def get_lockout_limit(self):
        return self._lockout_limit

    def get_warning_limit(self):
        return self._warning_limit



