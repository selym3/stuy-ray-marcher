from .measurable import Measurable

def repeat(primitive, period):
    def repeat_sdf(pos):
        looped = (pos % period) - (period * 0.5) 
        return primitive.sdf(looped)

    return Measurable(calculator=repeat_sdf)

def sphere(position, radius):
    def sphere_sdf(pos):
        return (pos - position).mag() - radius

    return Measurable(calculator=sphere_sdf)

def box(position, size):
    def box_sdf(pos):
        dxyz = ((pos - position).abs() - size).max(0)
        return dxyz.mag()
        # dx = max(abs(pos[0] - position[0]) - size[0], 0)
        # dy = max(abs(pos[1] - position[1]) - size[1], 0)
        # dz = max(abs(pos[2] - position[2]) - size[2], 0)
        # return math.sqrt(dx*dx + dy*dy + dz*dz)

    return Measurable(calculator=box_sdf)

def plane(n, h):
    n = n.normal()
    def plane_sdf(pos):
        return pos.dot(n) - h
        # dot = pos[0]*n[0] + pos[1]*n[1] + pos[2]*n[2]
        # return dot - h
    
    return Measurable(calculator=plane_sdf)

def group(objects):
    def group_sdf(pos):
        return min(
            object.sdf(pos) 
            for object 
            in objects
        )

    return Measurable(calculator=group_sdf)