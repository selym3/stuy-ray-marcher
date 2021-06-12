# TODO: clean up this file

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

    def missed(marched, closest=-1):
        return RayCollision(
            distance=marched, 
            collision=None, 
            normal=None, 
            closest=closest, 
            hit=False #<-- most important
        )

    def __init__(self, distance, collision, normal, closest=-1, hit=True):
        self.marched = distance

        self.collision = collision
        self.normal = normal

        self.closest = closest
        self.hit = hit

def MarchRay(ray, object, c=MarchConstraints.default()):
    marched = 0
    closest = float('+inf')

    hit = False

    for _ in range(c.max_steps):
        ray_end = ray.get_point(marched)

        from_surface = object.sdf(ray_end)
        closest = min(from_surface, closest)
        marched += from_surface

        if from_surface < c.surface_epsilon:
            hit = True
            break
        if marched > c.max_distance:
            hit = False
            break
            
    return RayCollision(
        distance = marched,
        collision = ray_end,
        normal = object.normal(ray_end) if hit else None,
        closest = closest,
        hit = hit
    )
