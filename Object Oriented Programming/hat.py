import random


class Hat:
    house = ["Dhaka", "Delhi", "London", "New York"]

    # Class variables
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.house)
        print(name, "is in", house)


Hat.sort("Tanvir")
