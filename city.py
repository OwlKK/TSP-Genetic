import numpy as np


class City:
    def __init__(self, posNum, x, y):
        self.posNum = posNum
        self.x = x
        self.y = y

    def distance(self, city):
        xDistance = abs(self.x - city.x)
        yDistance = abs(self.y - city.y)
        # added int
        distance = int(np.sqrt((xDistance ** 2) + (yDistance ** 2)))
        return distance

    # returns -> String object(value1, value2)
    # extra calculation so we get back at first city
    def __repr__(self):
        return "City" + str(self.posNum) + "_(" + str(self.x) + " " + str(self.y) + ")"
