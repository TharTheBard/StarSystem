class CelestialBody:
    def __init__(self, mass, radius, position):
        self.mass = mass
        self.radius = radius
        self.position = position

class Planet(CelestialBody):
    def __init__(self, mass, radius, position, velocityVector):
        super().__init__(mass, radius, position)
        self.velocityVector = velocityVector #Vector: Horizontal, Vertical | Unit: pixels/second
        self.isMovable = True

class Star(CelestialBody):
    def __init__(self, mass, radius, position, velocityVector = (0, 0)):
        super().__init__(mass, radius, position)
        self.velocityVector = velocityVector #Vector: Horizontal, Vertical | Unit: pixels/second
        self.isMovable = False