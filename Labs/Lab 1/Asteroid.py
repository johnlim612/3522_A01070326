
class Asteroid:
    count = 1;
    def __init__(self, metre, pos, vel):

        self._metre = metre
        self._pos = pos
        self._vel = vel
        self._id = self.count
        # counts number of asteroids made
        self.__class__.count += 1


    def get_metre(self):
        return self._metre

    def get_pos(self):
        return self._pos

    def get_vel(self):
        return self._vel

    def set_metre(self, circumference):
        self._metre = circumference

    def set_pos(self, pos):
        self._pos = pos

    def set_vel(self, vel):
        self._vel = vel

    def move(self):
        self._pos[0] += self._vel[0]
        self._pos[1] += self._vel[1]
        self._pos[2] += self._vel[2]

    def __str__(self):
        return (f"Asteroid {self._id} is currently at {self.get_pos()[0]}, {self.get_pos()[1]}, {self.get_pos()[2]} "
                f"and moving at {self.get_vel()[0]}, {self.get_vel()[1]}, {self.get_vel()[2]} metres per second. "
                f"It has a circumference of {self._metre}")



