from .marcher import MarchRay
from .ray import Ray
from utils import clamp
from constants import *

class Material:

    def __init__(self, specular, diffuse, ambient, shininess):
        self.specular = specular
        self.diffuse = diffuse
        self.ambient = ambient
        self.shininess = shininess

class Light:

    def __init__(self, position, color, brightness):
        self.position = position
        self.color = color
        self.brightness = brightness

    def get_lighting(self, object, hit, material):
        '''
        This function uses the Phong Reflection model to color a collision
        on an object. 

        The object paramter represents this object, and the collision represents
        where its being colored. It is assumed the collision was actually a hit.
        '''

        # Create a ray to the light source
        eps = 0.02
        to_light = (self.position - hit.at)
        light_ray = Ray(hit.at, to_light).correct(hit.normal, eps)

        # See if there are any other surfaces between the light source and
        # surface collided with. We march the ray and see if it traveled enough
        # distance to reach the light.
        if SHADOWS:
            light_collision = MarchRay(light_ray, object)
            in_shade = light_collision.marched < to_light.mag()
        else:
            in_shade = False

        brightness = material.ambient

        # Compute phong lighting and fresnel reflection if not in a shadow
        # (formulas just compiled from online)
        if not in_shade:
            normal = hit.normal
            light_dir = Ray(hit.at, -to_light).reflect(hit.normal).direction

            h = light_ray.direction
            l = (h - hit.coming_from).normal()

            f = (material.specular + (1 - material.specular) * (clamp(1 - h.dot(l), 0, 1))**5)

            brightness += (1 - f) * material.diffuse * max(0, normal.dot(h))
            brightness += (0 + f) * (max(0, -(hit.coming_from.dot(light_dir)))**material.shininess)

        return self.color * ((self.brightness * brightness) / (to_light.mag()**2))
