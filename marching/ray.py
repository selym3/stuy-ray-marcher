from utils import mag

class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction/mag(direction)

    def get_point(self, t):
        return self.origin + (self.direction * t)