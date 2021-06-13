from constants import *

class RayCollision:
    '''
    This is a structure that describes what happens at a collision (or a not collision)
    between a ray and an object.
    '''

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
        
        # Calculate distance to the scene and
        # accumulate the total distance 
        from_surface = object.sdf(ray_end)
        marched += from_surface

        # If gotten close enough to the surface, hit the scene
        if from_surface < SURFACE_DISTANCE:
            hit = True
            break
        
        # If marched past a cutoff, missed the scene
        if marched > MAX_DISTANCE:
            hit = False
            break
        
    # Return the collision object and only calculate normal if
    # a hit occured
    return RayCollision(
        distance = marched,
        collision = ray_end,
        from_dir = ray.direction,
        normal = object.normal(ray_end) if hit else None,
        hit = hit
    )
