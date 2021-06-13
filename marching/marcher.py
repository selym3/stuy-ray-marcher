from constants import *

class RayCollision:

    def __init__(self, distance, from_dir, collision, normal, hit):
        self.marched = distance
        self.collided = hit

        self.coming_from = from_dir
        self.at = collision
        self.normal = normal


def MarchRay(ray, object):
    marched = 0
    hit = False

    for _ in range(MAX_STEPS):
        ray_end = ray.get_point(marched)
        
        from_surface = object.sdf(ray_end)
        marched += from_surface

        if from_surface < SURFACE_DISTANCE:
            hit = True
            break
        if marched > MAX_DISTANCE:
            hit = False
            break
            
    return RayCollision(
        distance = marched,
        collision = ray_end,
        from_dir = ray.direction,
        normal = object.normal(ray_end) if hit else None,
        hit = hit
    )
