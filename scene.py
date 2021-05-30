from window import *
from pixels import *

from utils import random_color

class Scene:

    _Pixels = { 'fast': Pixels, 'slow': PixelDrawer }['fast']

    def __init__(self, width, height):
        self.window = Window(width, height)
        self.pixels = Scene._Pixels(width, height)

    def is_running(self):
        return self.window.running

    def execute(self):

        for x, y in self.pixels.cors():
            self.pixels.set_pixel(x, y, random_color())

        self.window.draw(self.pixels)