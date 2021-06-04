from .measurable import Measurable
import numpy as np
from utils import mag, norm

import math

def mod(primitive, period):
    ''' this might not work -- needs testing '''
    def mod_sdf(pos):
        half_pd = 0.5 * period
        looped = np.mod(pos + half_pd, period) - half_pd
        return primitive.sdf(looped)

    return Measurable(calculator=mod_sdf)

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