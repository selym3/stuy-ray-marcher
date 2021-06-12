class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normal() 

    def get_point(self, t):
        return self.origin + (self.direction * t)

    def correct(self, normal=None, epsilon=0.01):
        normal = self.direction if normal is None else normal

        return Ray(
            self.origin + normal * epsilon,
            self.direction
        )

    def reflect(self, normal, epsilon=0.01):
        return Ray(
            self.origin,
            self.direction - 2 * normal * (self.direction.dot(normal))
        ).correct(normal, epsilon)

    def __str__(self):
        return f"{self.origin} heading {self.direction}"