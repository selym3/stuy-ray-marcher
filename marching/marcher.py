# TODO: clean up this file

from utils import Vec3

class MarchConstraints:

    MaxSteps = int(1e3)
    MaxDistance = 1e3
    SurfaceEpsilon = 0.01

    def default():
        return MarchConstraints(
            MarchConstraints.MaxSteps,
            MarchConstraints.MaxDistance,
            MarchConstraints.SurfaceEpsilon
        )

    def __init__(self, max_steps, max_distance, surface_epsilon):
        self.max_steps = max_steps
        self.max_distance = max_distance
        self.surface_epsilon = surface_epsilon

class RayCollision:

    def missed(marched, attempts=-1):
        return RayCollision(
            distance=marched, 
            collision=None, 
            normal=None, 
            attempts=attempts, 
            hit=False #<-- most important
        )

    def __init__(self, distance, collision, normal, attempts=-1, hit=True):
        self.marched = distance

        self.collision = collision
        self.normal = normal

        self.attempts = attempts
        self.hit = hit

def MarchRay(ray, object, c=MarchConstraints.default()):
    marched = 0
    attempts = 0

    for _ in range(c.max_steps):
        ray_end = ray.get_point(marched)

        from_surface = object.sdf(ray_end)
        marched += from_surface

        attempts += 1

        if marched > c.max_distance or from_surface < c.surface_epsilon:
            break
            
    if marched > c.max_distance:
        return RayCollision.missed(marched, attempts)

    normal = object.normal(ray_end)

    return RayCollision(
        distance = marched,
        collision = ray_end,
        normal = normal,
        attempts = attempts,
        hit = from_surface < c.surface_epsilon
    )
