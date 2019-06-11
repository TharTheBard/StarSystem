from pygame import Rect

class Rectangle():
    def __init__(self, x, y, width, height):
        # super().__init__((x - width / 2, y - height / 2), (x + width / 2, y + height / 2))
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.half_width = width // 2
        self.half_height = height // 2
        self.quarter_width = width // 4
        self.quarter_height = height // 4

    def __str__(self):
        return f'Center: {self.x}|{self.y}  Width: {self.width}  Height: {self.height}'

    def contains(self, x, y):
        return self.x - self.half_width <= x < self.x + self.half_width and self.y - self.half_height <= y < self.y + self.half_height

class Polygon():
    def __init__(self, color, pointlist, width = 0):
        self.color = color
        self.pointlist = pointlist
        self.width = width

    def __str__(self):
        return self.pointlist
