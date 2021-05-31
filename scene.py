from graphics import *
from marching import *

from utils import random_color

class Scene:
    ''' 
    The scene is where the ray marching algorithm is run and 
    the graphics components are used to display it. 
    '''

    _Pixels = { 'fast': Pixels, 'slow': PixelDrawer }['fast']
    CanMarch = False

    def __init__(self, width, height, objects=[], camera=None):
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
        self.objects = objects

    def is_running(self):
        return self.window.running

    def execute(self):
        
        if Scene.CanMarch:
            for x, y in self.pixels.cors():
                # x and y may be in the wrong range
                ray = self.camera.generate_ray(x, y)
                color = MarchRay(ray, self.objects)

                self.pixels.set_pixel(x, y, color)
        else:
            for x, y in self.pixels.cors():
                self.pixels.set_pixel(x, y, random_color())

        self.window.draw(self.pixels)
