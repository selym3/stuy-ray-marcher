'''
See examples.py, constants.py, or main.py for configurable code.
'''

from graphics import *
from marching import *

import platform
if platform.system() in ( 'Windows', 'Darwin' ):
    import threading
    Worker = threading.Thread
else:
    import multiprocessing
    Worker = multiprocessing.Process

from utils import clamp
from vec3 import Vec3

from constants import *

class Scene:
    ''' 
    The scene is where the ray marching algorithm is run and 
    the graphics components are used self.buffer = np.ndarray((height,width,3), dtype=np.uint8)to display it. 
    '''

    _Pixels = { 
        'fast': Pixels, 
        'slow': PixelDrawer,
        'test': PixelBase
    }['fast']
    
    def __init__(self, object, lights):
        # Turtle Rendering
        self.window = Window(WIDTH, HEIGHT)
        self.pixels = Scene._Pixels(RESOLUTION[0], RESOLUTION[1])
        
        # Raymarching Calculations
        self.camera = Camera(
            RESOLUTION[0], RESOLUTION[1],
            position=Vec3(*POSITION),
            angle=[ math.radians(c) for c in ANGLE ],
            fov=FOV
        )

        self.object = object
        self.lights = lights

        self.material = Material(
            SPECULAR,
            DIFFUSE,
            AMBIENT,
            SHININESS
        )

        if THREADS > 1:
            self.update_pixels = lambda: self.update_pixels_multi(THREADS)
        else:
            self.update_pixels = lambda: self.update_pixels()

    def is_running(self):
        return self.window.running

    def execute(self):
        self.update_pixels()
        self.window.draw(self.pixels)

    def get_pixel(self, x, y):
        ray = self.camera.get_ray(x, y)
        hit = MarchRay(ray, self.object)

        if hit.collided:
            return self.get_color_phong(hit)
        else:
            return Vec3(*BACKGROUND_COLOR)

    def get_color_normal(self, hit):
        return 255 * (hit.normal * 0.5 + 0.5)

    def get_color_phong(self, hit):
        base_color = Vec3(0,0,0)

        for light in self.lights:
            base_color += light.get_lighting(self.object, hit, self.material)

        return base_color

    def update_pixels_single(self):
        for x, y in self.pixels.cors():
            self.pixels.set_pixel(x, y, self.get_pixel(x,y))

    def update_pixels_multi(self, thread_count):
        thread_count = clamp(thread_count, 0, self.pixels.height)
        coords = list(self.pixels.cors())

        def on_thread(which, thread_count):
            for x, y in coords[which::thread_count]:
                try:
                    color = self.get_pixel(x, y)
                    self.pixels.set_pixel(x, y, color)
                except Exception as e: 
                    self.window._stop_running()
                    raise e

        thread_pool = []

        for which in range(thread_count):
            thread = Worker(target=on_thread, args=(which, thread_count))
            thread_pool += [thread]
            thread.start()

        for thread in thread_pool:
            if ANIMATE_FILL:
                while thread.is_alive():
                    self.window.draw(self.pixels)
            thread.join()