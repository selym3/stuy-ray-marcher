import turtle
import numpy as np
from PIL import Image
from time import time

from multiprocessing import shared_memory
import os

from utils import Traversable, toColor

from constants import *

class PixelBase(Traversable):
    '''
    A class that represents a drawable 2D grid of pixels.

    This base class is not technically necessary but it shows
    what methods are common and enforces the Traversable/width, height
    rather than leaving it to duck typing
    '''
    def __init__(self, width, height):
        super().__init__(0, 0, width, height)
        self.width, self.height = width, height

    def set_pixel(self, x, y, color):
        # raise NotImplementedError
        pass
    def draw(self, window):
        # raise NotImplementedError
        pass

class PixelDrawer(PixelBase):
    '''
    A class that represents a drawable 2D Grid of pixels.

    This class works by having an interal pen move around
    the screen and adjusting its color to set the proper pixels.

    (NOTE: clearing is not automatically handled by this class. everything
    must be drawn over. a modication to the implementation can allow this 
    by having an internal array of colors, but this method is slow anyway)
    '''

    def __init__(self, width, height):
        super().__init__(width, height)
        
        self.pen = turtle.Turtle()
        self.pen.ht()
        self.pen.pu()

    def clear(self):
        self.pen.clear() 

    def set_pixel(self, x, y, color):
        self.pen.goto(x - self.width//2, y - self.width//2)
        self.pen.dot(1, color)
    
    def draw(self, window):
        pass

class Pixels(PixelBase):
    ''' 
    A class that represents a drawable 2D Grid of pixels.

    The class works by having an internal turtle and whenever
    a draw call is made, the grid is made into an image and the 
    turtle's shape becomes the image.
    '''

    SaveImage = None # 'images/new_frame.png'
    ResizeImage = (300,300)

    def __init__(self, width, height, shapename=None):
        super().__init__(width, height)

        # Setup turtle
        self.pen = turtle.Turtle()
        self.pen.goto(0, 0)
        self.pen.ht()

        # Decide on a shapename to use (so that all pixel
        # instances have different shapenames)
        self.shapename =  \
            str(int(time() * 1_000_000)) \
            if shapename is None \
            else shapename

        # Create a buffer to modify it and convert into 
        # an image
        
        if self.needs_multi_processing():
            buffer = np.empty(
                (height, width, 3),
                dtype=np.uint8
            )

            self.shm = shared_memory.SharedMemory(create=True, size=buffer.nbytes)

            self.buffer = np.ndarray(
                (height, width, 3),
                dtype=np.uint8,
                buffer=self.shm.buf
            )
        else:
            self.buffer = np.ndarray((height,width,3), dtype=np.uint8)

    def needs_multi_processing(self):
        return os.name != 'nt'

    def __del__(self):
        del self.buffer
        self.shm.close()
        self.shm.unlink()

    def clear(self):
        # I don't use this, but it helps show how this 
        # class works. It is controlled by a single turtle 
        # with a shape
        self.pen.ht()

    def set_pixel(self, x, y, color):
        # Place a color in a numpy array
        color = toColor(color)
        self.buffer[y, x] = color

    def to_image(self):
        image = Image.fromarray(self.buffer, mode='RGB')

        if RESOLUTION:
            image = image.resize((WIDTH, HEIGHT))

        if type(SAVE_AS) == str:
            image.save(SAVE_AS)
        
        return image

    def draw(self, window):
        
        # Replace the pixel's entry in the shape dictionary
        # with a (potentially) different image
        window.add_pil(
            self.shapename, 
            self.to_image()
        )

        # Modify a turtle (that should be in the center)
        # and set the new image as its shape
        self.pen.shape(self.shapename)
        self.pen.st()
