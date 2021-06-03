from .ray import Ray 
from utils import Vec3

import math

class Camera:

    def __init__(self, width, height, position, angle=(0,0,0), fov=90.0):
        '''
        TODO: use this data to take into account camera position
        and angle and fov
        '''

        self.width, self.height = width, height
        
        self.position = Vec3(*position)
        self.yaw, self.pitch, self.roll = angle
        self.fov = fov

    def generate_ray(self, pixel_x, pixel_y):
        ''' TODO: change this to take into account fov and pos, angle '''
        
        ratio = self.height/self.width
        angle = math.tan(math.radians(self.fov/2)) 

        sx = 2 * ((pixel_x + 0.5) / self.width) - 1
        sx *= 1
        sx *= angle

        sy = 1 - 2 * (pixel_y + 0.5) / self.height
        sy *= ratio
        sy *= angle

        return Ray(
            self.position,
            Vec3(sx, sy, +1)
        )