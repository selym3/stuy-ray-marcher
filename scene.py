from graphics import *
from marching import *

import threading

from utils import clamp
from vec3 import Vec3

import copy

class Scene:
    ''' 
    The scene is where the ray marching algorithm is run and 
    the graphics components are used to display it. 
    '''

    _Pixels = { 
        'fast': Pixels, 
        'slow': PixelDrawer,
        'test': PixelBase
    }['fast']
    
    def __init__(self, width, height, light, objects, camera=None):
        # Turtle API
        self.window = Window(width, height)
        self.pixels = Scene._Pixels(width, height)
        
        # Raymarching API
        if camera is None:
            camera = Camera(
                width, height, 
                position=Vec3(0,0,0),
                fov=90
            )

        self.camera = camera 
        # self.objects = group(objects)
        self.objects = objects

        self.light = light

        self.t = 0

    def is_running(self):
        return self.window.running

    def update_camera(self):
        self.camera.position = Vec3(
            math.cos(self.t) * 4,
            3,
            math.sin(self.t) * 4
        )

        self.camera.angle = (0, self.t, 0)
        self.t += 0.05 * 4

    def execute_multi(self, thread_count=16):
        self.update_pixels_multi(thread_count)
        self.window.draw(self.pixels)
        self.update_camera()

    def execute(self):
        self.update_pixels()
        self.window.draw(self.pixels)

    def get_pixel(self, x, y):
        ray = self.camera.get_ray(x, y)
        c = MarchRay(ray, self.objects)

        if c.hit:
            return self.light.get_lighting(self.objects, c)
            # return Vec3(255, 255, 255)
        else:
            return Vec3(0,0,0)

    def update_pixels(self):
        for x, y in self.pixels.cors():
            self.pixels.set_pixel(x, y, self.get_pixel(x,y))

    def update_pixels_multi(self, thread_count):
        thread_count = clamp(thread_count, 0, self.pixels.height)
        per_thread = int( 0.5 + self.pixels.height / thread_count)

        def on_thread(start, end):
            camera = copy.deepcopy(self.camera)
            light = copy.deepcopy(self.light)
            objects = copy.deepcopy(self.objects)

            xcors = list(self.pixels.xcors())

            for y in range(start, end):
                for x in xcors:
                    try:
                        ray = camera.get_ray(x, y)
                        c = MarchRay(ray, objects)

                        if c.hit:
                            color = light.get_lighting(objects, c)
                            # return Vec3(255, 255, 255)
                        else:
                            color = Vec3(0,0,0)
                        
                        self.pixels.set_pixel(x, y, color)

                    except Exception as e: print(e)

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
            while thread.is_alive():
                self.window.draw(self.pixels)
            thread.join()
