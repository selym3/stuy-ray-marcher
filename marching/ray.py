from utils import Vec3, norm

class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = norm(direction)

    def get_point(self, t):
        px = self.origin[0] + self.direction[0]*t
        py = self.origin[1] + self.direction[1]*t
        pz = self.origin[2] + self.direction[2]*t

        return Vec3(px,py,pz)

        # return self.origin + (self.direction * t)

    def __str__(self):
        return f"{self.origin} heading {self.direction}"