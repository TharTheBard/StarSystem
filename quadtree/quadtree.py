from.shapes import Rectangle

class QuadTree:
    def __init__(self, boundary: Rectangle, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.objects = []
        self.divided = False

    def insert(self, object):
        if not self.boundary.contains(object.position[0], object.position[1]):
            return

        if len(self.objects) < self.capacity:
            self.objects.append(object)
        else:
            if not self.divided:
                self.subdivide()

            self.northwest.insert(object)
            self.northeast.insert(object)
            self.southwest.insert(object)
            self.southeast.insert(object)

    def subdivide(self):
        _ = self.boundary
        self.northwest = QuadTree(Rectangle(_.x - _.quarter_width, _.y - _.quarter_height, _.half_width, _.half_height),
                                  self.capacity)
        self.northeast = QuadTree(Rectangle(_.x + _.quarter_width, _.y - _.quarter_height, _.half_width, _.half_height),
                                  self.capacity)
        self.southwest = QuadTree(Rectangle(_.x - _.quarter_width, _.y + _.quarter_height, _.half_width, _.half_height),
                                  self.capacity)
        self.southeast = QuadTree(Rectangle(_.x + _.quarter_width, _.y + _.quarter_height, _.half_width, _.half_height),
                                  self.capacity)
        self.divided = True
