import random


class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight_len = 0

    def wings(self):
        if random.radint(2, 6, 2) == 2:
            self.wings = 2
        else:
            self.legs = 4

    def get_info():
        return self.wings
        reutrn self.legs
