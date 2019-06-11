class CelestialBody:
    def __init__(self, mass, radius, centre_of_mass):
        self.mass = mass
        self.radius = radius
        self.centre_of_mass = centre_of_mass
        self.force = 0


class Planet:
    def __init__(self, mass, radius, centre_of_mass, velocity):
        self.mass = mass
        self.radius = radius
        self.centre_of_mass = centre_of_mass
        self.force = 0
        self.velocity = velocity

        self.is_movable = True


class Star:
    def __init__(self, mass, radius, centre_of_mass, velocity=(0, 0)):
        self.mass = mass
        self.radius = radius
        self.centre_of_mass = centre_of_mass
        self.force = 0
        self.velocity = velocity

        self.is_movable = False
