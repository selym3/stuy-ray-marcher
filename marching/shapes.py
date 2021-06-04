from .measurable import Measurable
from utils import Vec3, norm, mod, mag

import math

def repeat(primitive, period):
    def repeat_sdf(pos):
        looped = mod(pos, period)
        half_pd = Vec3(period[0]*0.5, period[1]*0.5, period[2]*0.5)
        looped = Vec3(looped[0] - half_pd[0], looped[1] - half_pd[1], looped[2] - half_pd[2])
        return primitive.sdf(looped)

    return Measurable(calculator=repeat_sdf)

def sphere(position, radius):
    def sphere_sdf(pos):
        dx = pos[0] - position[1]
        dy = pos[1] - position[1]
        dz = pos[2] - position[2]
        return math.sqrt(dx*dx + dy*dy + dz*dz) - radius

    return Measurable(calculator=sphere_sdf)

def box(position, size):
    def box_sdf(pos):
        dx = max(abs(pos[0] - position[0]) - size[0], 0)
        dy = max(abs(pos[1] - position[1]) - size[1], 0)
        dz = max(abs(pos[2] - position[2]) - size[2], 0)

        return math.sqrt(dx*dx + dy*dy + dz*dz)

    return Measurable(calculator=box_sdf)

def plane(n, h):
    n = norm(n)
    def plane_sdf(pos):
        dot = pos[0]*n[0] + pos[1]*n[1] + pos[2]*n[2]
        return dot - h
    
    return Measurable(calculator=plane_sdf)

def group(objects):
    def group_sdf(pos):
        return min(
            object.sdf(pos) 
            for object 
            in objects
        )

    return Measurable(calculator=group_sdf)