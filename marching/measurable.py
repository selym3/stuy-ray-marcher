class Measurable:
    def __init__(self, calculator):
        self.calculator = calculator
    
    #######################
    # DISTANCE CALCULATOR #
    #######################

    def sdf(self, pos):
        ''' Calculate distance to the end of a camera ray '''
        return self.calculator(pos)

    # needs a way to find a surface normal

    ###############################
    # CONSTRUCTIVE SOLID GEOMETRY #
    ###############################

    def __or__(self, other):
        ''' Union of two measurable objects '''
        return Measurable(lambda pos:
            min(
                self.sdf(pos),
                other.sdf(pos)        
            )
        )
    
    def __and__(self, other):
        ''' Intersection of two measurable objects '''
        return Measurable(lambda pos:
            max(
                self.sdf(pos),
                other.sdf(pos)
            )
        )

    def __not__(self):
        ''' Negation of a measurable object '''
        return Measurable(lambda pos: -self.sdf(pos))