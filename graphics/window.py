import turtle
from PIL import ImageTk

from utils import Traversable

class Window(Traversable):
    '''
    A class wrapper for the turtle screen singleton
    with extra necessary methods. 

    The class assumes the window takes on one size, sets up a escape
    key exit, allows for image based shapes outside of .GIF,
    and provides convenience iterators for traversal.
    ''' 

    def __init__(self, width, height):
        super().__init__(
            -width//2, -height//2,
            +width//2, +height//2
        )

        self.screen = turtle.Screen()
        self.screen.colormode(255)

        self.width = width
        self.height = height

        self.screen.setup(width, height)

        self.running = True

        self.screen.listen()
        self.screen.onkeypress(self._stop_running, "Escape")

    def _stop_running(self):
        self.running = False

    def clear(self):
        # this shouldn't be used because it breaks turtles
        self.screen.clear()
        self.screen.colormode(255)

    def draw(self, drawable):
        # A (assumed) interface has a draw method that takes in
        # an instance of this window class. This is a convenience
        # method to use that interface
        drawable.draw(self)

    def add_pil(self, name, im):
        # Avoid saving a PIL.Image object as a gif to be used
        self.screen._shapes[name] = turtle.Shape("image", ImageTk.PhotoImage(im))

    def del_pil(self, name):
        # Delete a shape -- not really a necessary method
        del self.screen._shapes[name]