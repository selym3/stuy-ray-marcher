from graphics import *
from marching import *

import threading

from utils import clamp
from vec3 import Vec3

class Scene:
    ''' 
    The scene is where the ray marching algorithm is run and 
    the graphics components are used to display it. 
    '''

    _Pixels = { 
        'fast': Pixels, 
        'slow': PixelDrawer
    }['fast']
    
    def __init__(self, width, height, objects=[], light=Vec3(0,0,0), camera=None):
        # Turtle API
        self.window = Window(width, height)
        self.pixels = Scene._Pixels(width, height)
        
        # Raymarching API
        if camera is None:
            camera = Camera(
                width, height, 
                position=(0,0,0),
                fov=90
            )

        self.camera = camera 
        self.objects = group(objects)

        self.light = light

    def is_running(self):
        return self.window.running

    def execute_multi(self, thread_count=16):
        self.update_pixels_multi(thread_count)
        self.window.draw(self.pixels)

    def execute(self):
        self.update_pixels()
        self.window.draw(self.pixels)

    def get_pixel(self, x, y):
        ray = self.camera.generate_ray(x, y)
        c = MarchRay(ray, self.objects)

        if c.hit:
            return Vec3(255, 255, 255)
        else:
            return Vec3(0,0,0)

    def update_pixels(self):
        for x, y in self.pixels.cors():
            self.pixels.set_pixel(x, y, self.get_pixel(x,y))

    def update_pixels_multi(self, thread_count):
        thread_count = clamp(thread_count, 0, self.pixels.height)
        per_thread = int( 0.5 + self.pixels.height / thread_count)

        def on_thread(start, end):
            for y in range(start, end):
                for x in self.pixels.xcors():
                    color = self.get_pixel(x, y)
                    self.pixels.set_pixel(x, y, color)

        thread_pool = []

        which = 0
        for which in range(thread_count):
            start = clamp((which + 0) * per_thread, 0, self.pixels.height)
            end   = clamp((which + 1) * per_thread, 0, self.pixels.height)

            if which+1 == thread_count:
                end = self.pixels.height

            thread = threading.Thread(target=on_thread, args=(start, end))
            thread_pool += [thread]
            thread.start()

        for thread in thread_pool:
            thread.join()