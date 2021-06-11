from .ray import Ray 
from vec3 import Vec3

import math

class Camera:

    def __init__(self, width, height, position, angle=(0,0,0), fov=90.0):
        self.width, self.height = width, height
        self.ratio = height/width

        self.position = position
        # self.yaw, self.pitch, self.roll = angle
        self.angle = angle
        
        self.fov = fov
        self.fov_scalar = math.tan(math.radians(self.fov/2)) 

    def get_ray(self, pixel_x, pixel_y):
        sx = self.fov_scalar * (2 * ((pixel_x + 0.5) / self.width) - 1)

        sy = self.ratio * self.fov_scalar * (1 - 2 * (pixel_y + 0.5) / self.height)

        direction = Vec3(sx, sy, +1).rotate(*self.angle)

        return Ray(
            self.position,
            direction
        )