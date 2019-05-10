from pygame import Rect

class Rectangle(Rect):
    def __init__(self, center_x, center_y, width, height):
        super().__init__((center_x - width / 2, center_y - height / 2), (center_x + width / 2, center_y + height / 2))
