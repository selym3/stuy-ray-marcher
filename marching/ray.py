class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normal() 

    def get_point(self, t):
        return self.origin + (self.direction * t)

    def __str__(self):
        return f"{self.origin} heading {self.direction}"