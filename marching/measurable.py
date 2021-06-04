from utils import Vec3, norm

class Measurable:
    def __init__(self, calculator):
        self.calculator = calculator
    
    #######################
    # DISTANCE CALCULATOR #
    #######################

    def sdf(self, pos):
        ''' Calculate distance to the end of a camera ray '''
        return self.calculator(pos)

    def normal(self, pos, epsilon=0.1):
        ''' Calculates a collision normal at an assumed collision point '''
        dist = self.sdf(pos)

        # Moves a small distance in each direction on the surface
        # of the object to estimate a normal at the position
        normal = Vec3(
            dist - self.sdf(Vec3(pos[0] - epsilon, pos[1], pos[2])),
            dist - self.sdf(Vec3(pos[0], pos[1] - epsilon, pos[2])),
            dist - self.sdf(Vec3(pos[0], pos[1], pos[2] - epsilon))
        )

        return norm(normal)

    ###############################
    # CONSTRUCTIVE SOLID GEOMETRY #
    ###############################

    def __add__(self, other):
        ''' Union of two measurable objects '''
        return Measurable(lambda pos:
            min(
                self.sdf(pos),
                other.sdf(pos)        
            )
        )
    
    def __mul__(self, other):
        ''' Intersection of two measurable objects '''
        return Measurable(lambda pos:
            max(
                self.sdf(pos),
                other.sdf(pos)
            )
        )

    def __invert__(self):
        ''' Negation of a measurable object '''
        return Measurable(lambda pos: -self.sdf(pos))

    def __sub__(self, other):
        ''' Difference between two measurable objects '''
        return self * (~other)
