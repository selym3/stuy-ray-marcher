from .measurable import Measurable

def mod(primitive, period):
    def mod_sdf(pos):
        looped = (pos % period) - (period * 0.5) 
        return primitive.sdf(looped)

    return Measurable(calculator=mod_sdf)

def sphere(position, radius):
    def sphere_sdf(pos):
        return (pos - position).mag() - radius

    return Measurable(calculator=sphere_sdf)

def box(position, size):
    def box_sdf(pos):
        dxyz = ((pos - position).abs() - size).max(0)
        return dxyz.mag()

    return Measurable(calculator=box_sdf)

def plane(n, h):
    n = n.normal()
    def plane_sdf(pos):
        return pos.dot(n) - h
    
    return Measurable(calculator=plane_sdf)