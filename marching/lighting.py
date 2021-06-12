from .marcher import MarchRay
from .ray import Ray
from utils import clamp
from vec3 import Vec3

class Material:

    def __init__(self, specular, diffuse, ambient, shininess):
        self.specular = specular
        self.diffuse = diffuse
        self.ambient = ambient
        self.shininess = shininess

class Light:

    def __init__(self, position, color=Vec3(255, 255, 255)):
        self.position = position
        self.color = color

    def get_lighting(self, obj, c):
        # c is a collision object that will help create
        # a ray from the surface point to the light

        eps = 0.2
        to_light = (self.position - c.collision)
        light_ray = Ray(c.collision, to_light).correct(c.normal, eps)

        # Perform the collision here, it will give us a distance marched
        light_collision = MarchRay(light_ray, obj)

        # Calculate the illumination of the surface based on its 
        # normal and the direction to the light
        illumination = clamp(light_ray.direction.dot(c.normal), 0, 1)
        
        # The surface is in the shade if a ray from the surface didn't
        # travel the distance of the light ray
        if light_collision.marched < to_light.mag():
            illumination *= 0.1
        illumination **= 0.4545 #<-- gamma correction

        return self.color * illumination 

