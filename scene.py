from graphics import *
from marching import *

import threading

from utils import Vec3, clamp, mag

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

    def get_color(self, c):
        if not c.hit:
            # Configurable options
            max_glow_dist = 1
            glow_power = 0.1
            glow_color = Vec3(255, 0, 0) 

            # Calculate glow
            glow_power *= 255
            glow_coeff = c.closest/max_glow_dist
            glow_coeff *= (256 - glow_power)

            glow_color = Vec3(
                glow_color[0] / glow_coeff,
                glow_color[1] / glow_coeff,
                glow_color[2] / glow_coeff
            )

            return glow_color
            
        light_color = self.get_light(c)

        return light_color
    
    def get_light(self, c):
        ''' diffuse lighting algorithm '''
        to_light = Vec3(self.light[0] - c.collision[0], self.light[1] - c.collision[1], self.light[2] - c.collision[2])
        corrected = Vec3(c.collision[0] + 0.2*c.normal[0], c.collision[1] + 0.2*c.normal[1], c.collision[2] + 0.2*c.normal[2])
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

    def update_pixels(self):
        for x, y in self.pixels.cors():
            ray = self.camera.generate_ray(x, y)
            
            collision = MarchRay(ray, self.objects)
            color = self.get_color(collision)

            self.pixels.set_pixel(x, y, color)

    def update_pixels_multi(self, thread_count):
        thread_count = clamp(thread_count, 0, self.pixels.height)
        per_thread = int( 0.5 + self.pixels.height / thread_count)

        def on_thread(start, end):
            for y in range(start, end):
                for x in self.pixels.xcors():
                    ray = self.camera.generate_ray(x, y)
            
                    collision = MarchRay(ray, self.objects)
                    color = self.get_color(collision)

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