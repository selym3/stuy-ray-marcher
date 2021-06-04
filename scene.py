from graphics import *
from marching import *

import threading

from utils import Vec3, clamp
import numpy as np

class Scene:
    ''' 
    The scene is where the ray marching algorithm is run and 
    the graphics components are used to display it. 
    '''

    _Pixels = { 
        'fast': Pixels, 
        'slow': PixelDrawer,
        'test': NoPixels
    }['fast']
    
    CanMarch = True

    def __init__(self, width, height, objects=[], light=Vec3(0,0,0), camera=None):
        # Turtle API
        self.window = Window(width, height)
        self.pixels = Scene._Pixels(width, height)
        
        # Raymarching API
        if camera is None:
            camera = Camera(
                width, height, 
                position=(0,0,0)
            )

        self.camera = camera 
        self.objects = group(objects)

        self.light = light

    def is_running(self):
        return self.window.running

    def execute(self):
        for x, y in self.pixels.cors():
            ray = self.camera.generate_ray(x, y)
            
            collision = MarchRay(ray, self.objects)
            color = self.get_color(collision)

            self.pixels.set_pixel(x, y, color)

        self.window.draw(self.pixels)

    def get_color(self, c):
        if not c.hit:
            return Vec3(0,0,0)
            
        # normal_color = np.abs((c.normal * 255))
        light_color = self.get_light(c)

        return light_color # * normal_color
    
    def get_light(self, c):
        ''' diffuse lighting algorithm '''
        to_light = self.light - c.collision
        corrected = c.collision + (0.2 * c.normal)
        light_ray = Ray(corrected, to_light)

        ld = light_ray.direction
        light_coeff = ld[0]*c.normal[0] + ld[1]*c.normal[1] + ld[2]*c.normal[2]
        light_coeff = clamp(light_coeff, 0, 1)

        light_c = MarchRay(light_ray, self.objects)
        if light_c.marched < mag(to_light):
            light_coeff *= 0.1
        
        light_coeff **= .4545 # <-- gamma correction
        light_coeff = int(light_coeff * 255)

        return Vec3(light_coeff,light_coeff,light_coeff)