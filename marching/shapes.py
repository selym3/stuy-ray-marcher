from .measurable import Measurable

'''
See modifiers.py for cool things to add primitive shapes
See measurable.py for operators/modifiers with constructive solid geometry
'''

def sphere(position, radius):
    def sphere_sdf(pos):
        return (pos - position).mag() - radius

    return Measurable(calculator=sphere_sdf)

def box(position, size):
    ''' size is vec3 or a number ''' 
    def box_sdf(pos):
        dxyz = ((pos - position).abs() - size).max(0)
        return dxyz.mag()

    return Measurable(calculator=box_sdf)

def plane(n, h):
    ''' n is the surface direction of the plane, and h is a y intercept '''

    n = n.normal()
    def plane_sdf(pos):
        return pos.dot(n) - h
    
    return Measurable(calculator=plane_sdf)

def gyroid(bias=0.0):
    def gyroid_sdf(pos):
        s = pos.sin()
        c = (pos.zxy).cos()

        return abs(s.dot(c) - bias)

    return Measurable(calculator=gyroid_sdf)
