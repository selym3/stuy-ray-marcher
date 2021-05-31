import random
def random_color():
    ''' generates a tuple with 3 components in the range [0,255] '''

    return [
        random.randint(0, 255) 
        for _ in range(3)
    ]

def validate_color(color):
    '''
    tries to make a valid color out of a tuple

    rules:
    - will clamp values to [0,255] in a size 3 tuple
    - will throw error in tuple smaller than 3
    - will cutoff tuple if larger than 3
    '''

    return tuple(
        max(0, min(color[n], 255))
        for n
        in range(3)
    )

class Traversable:
    '''
    a convenience class for classes that represent 
    any 2D space that allows iteration over the x-
    y-axes and also every point.  
    
    the class should extent Traversable and provide min
    and max x- and y- coordinates.
    '''

    def __init__(self, minx=0, miny=0, maxx=0, maxy=0):
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy

    def min_xcor(self):
        return self.minx
    def max_xcor(self):
        return self.maxx
    def min_ycor(self):
        return self.miny
    def max_ycor(self):
        return self.maxy
    
    def xcors(self):
        return range(self.min_xcor(), self.max_xcor())
    def ycors(self):
        return range(self.min_ycor(), self.max_ycor())
    
    def cors(self):
        for y in self.ycors():
            for x in self.xcors():
                yield x, y
