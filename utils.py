import random
def random_color():
    return [
        random.randint(0, 255) 
        for _ in range(3)
    ]

class Traversable:
    
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