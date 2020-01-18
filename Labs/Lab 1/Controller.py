import random
import math
import datetime
import time

from Asteroid import Asteroid


class Controller:

    def __init__(self):
        # Creates list of asteroids
        self._asteroids = []
        # Inserts random asteroids in list
        for x in range(100):
            self._asteroids.append(self.random_asteroid())

    # generate random asteroid
    def random_asteroid(self):
        rad = random.randint(1, 4)
        circumference = math.pi * rad * 2
        pos = [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)]
        vel = [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)]

        return Asteroid(circumference, pos, vel)

    # Delays time perfectly on a second.
    def perfect_second(self):
        init_time = datetime.datetime.now()
        set_time = (1000000 - init_time.microsecond) / 1000000
        time.sleep(set_time)

    def simulate(self, seconds):
        self.perfect_second()
        current_time = datetime.datetime.now()
        print(f"Simulation Start Time: {current_time}\n\nMoving Asteroids!\n-----------------")

        # loops for each second
        for y in range(1, seconds + 1):
            self.perfect_second()

            # loops through each asteroid
            for x in self._asteroids:
                # gets initial asteroid position
                asteroid_init_pos = (x.get_pos()[0], x.get_pos()[1], x.get_pos()[2])
                print(f"Asteroid {x._id} Moved! Old Pos: {asteroid_init_pos} -> ", end="")
                x.move()

                # gets new asteroid position
                asteroid_new_pos = (x.get_pos()[0], x.get_pos()[1], x.get_pos()[2])
                print(f"New Pos: {asteroid_new_pos}")
                # print Asteroid __str__ method
                print(x)


def main():
    chicken = Controller()
    chicken.simulate(4)


if __name__ == '__main__':
    main()
