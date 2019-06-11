from.shapes import Rectangle
from content import physics

class QuadTree:
    def __init__(self, boundary: Rectangle, capacity=1):
        self.boundary = boundary
        self.capacity = capacity
        self.objects = []
        self.divided = False
        self.marked = False

        self.northwest = None
        self.northeast = None
        self.southwest = None
        self.southeast = None

        self.mass = None
        self.centre_of_mass = (boundary.x, boundary.y)

    def insert(self, solar_object):
        if not self.boundary.contains(solar_object.centre_of_mass[0], solar_object.centre_of_mass[1]):
            return

        if len(self.objects) < self.capacity and not self.divided:
            self.objects.append(solar_object)
        else:
            if not self.divided:
                self.subdivide()
                self.northwest.insert(self.objects[0])
                self.northeast.insert(self.objects[0])
                self.southwest.insert(self.objects[0])
                self.southeast.insert(self.objects[0])

            self.northwest.insert(solar_object)
            self.northeast.insert(solar_object)
            self.southwest.insert(solar_object)
            self.southeast.insert(solar_object)

            self.objects = []

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

    def calc_centre_of_mass(self):
        if self.divided:
            self.northwest.calc_centre_of_mass()
            self.northeast.calc_centre_of_mass()
            self.southwest.calc_centre_of_mass()
            self.southeast.calc_centre_of_mass()

            self.mass = self.northwest.mass + self.northeast.mass + self.southwest.mass + self.southeast.mass
            self.centre_of_mass = physics.n_body_centre_of_mass(
                self.northwest, self.northeast, self.southwest, self.southeast,
            )
        else:
            try:
                self.mass = self.objects[0].mass
                self.centre_of_mass = self.objects[0].centre_of_mass
            except IndexError:
                self.mass = 0
                self.centre_of_mass = (self.boundary.x, self.boundary.y)
