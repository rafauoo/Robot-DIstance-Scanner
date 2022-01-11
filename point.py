import math


class Point:
    def __init__(self, x, y) -> None:
        "creates instance of point"
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distance(self, other):
        "returns distance between two points"
        distance_x = abs(self.x() - other.x())
        distance_y = abs(self.y() - other.y())
        return math.sqrt(distance_x ** 2 + distance_y ** 2)
