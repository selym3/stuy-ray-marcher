import turtle
import numpy as np
from PIL import Image
from time import time

from utils import Traversable

# class Drawable:
#     def draw(self, window):
#         raise NotImplementedError
# class PixelBase(Traversable, Drawable):
#     pass

class PixelDrawer(Traversable):

    def __init__(self, width, height):
        super().__init__(
            -width//2, -height//2,
            +width//2, +height//2
        )
        
        self.width = width
        self.height = height

        self.pen = turtle.Turtle()
        self.pen.ht()
        self.pen.pu()

    def clear(self):
        self.pen.clear() 

    def set_pixel(self, x, y, color):
        self.pen.goto(x, y)
        self.pen.dot(1, color)
    
    def draw(self, window):
        pass


def validate_color(color):
    # will clamp values in a size 3 tuple
    # will throw error in tuple smaller than 3
    # will cutoff tuple if larger than 3

    return tuple(
        max(0, min(color[n], 255))
        for n
        in range(3)
    )

class Pixels(Traversable):

    def __init__(self, width, height, shapename=None):
        super().__init__(
            0, 0,
            width, height
        )

        self.width = width
        self.height = height

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

        # Create a buffer to modify and convert into 
        # an image
        self.buffer = np.empty(
            (width, height, 3),
            dtype=np.int8
        )

    def clear(self):
        # I don't use this, but it helps show how this 
        # class works. It is controlled by a single turtle 
        # with a shape
        self.pen.ht()

    def set_pixel(self, x, y, color):
        color = validate_color(color)
        self.buffer[x, y] = color

    def to_image(self):
        return Image.fromarray(self.buffer, mode='RGB')

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
