import math


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


    def get_x(self):
        return self.x


    def get_y(self):
        return self.y


    def change_position_x(self, position_x):
        self.x = position_x


    def change_position_y(self, position_y):
        self.y = position_y


    def distance(self, x2, y2):
        return math.hypot(self.x - x2, y2 - self.y)