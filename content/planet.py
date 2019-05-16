class CelestialBody:
    def __init__(self, mass, radius, centre_of_mass):
        self.mass = mass
        self.radius = radius
        self.centre_of_mass = centre_of_mass

class Planet(CelestialBody):
    def __init__(self, mass, radius, centre_of_mass, velocityVector):
        super().__init__(mass, radius, centre_of_mass)
        self.velocityVector = velocityVector #Vector: Horizontal, Vertical | Unit: pixels/second
        self.isMovable = True

class Star(CelestialBody):
    def __init__(self, mass, radius, centre_of_mass, velocityVector = (0, 0)):
        super().__init__(mass, radius, centre_of_mass)
        self.velocityVector = velocityVector #Vector: Horizontal, Vertical | Unit: pixels/second
        self.isMovable = False