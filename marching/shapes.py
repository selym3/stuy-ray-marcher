from .measurable import Measurable
import numpy as np
from utils import mag, norm

def mod(primitive, period):
    ''' this might not work -- needs testing '''
    def mod_sdf(pos):
        half_pd = 0.5 * period
        looped = np.mod(pos + half_pd, period) - half_pd
        return primitive.sdf(looped)

    return Measurable(calculator=mod_sdf)

def sphere(position, radius):
    def sphere_sdf(pos):
        diff = pos - position
        return mag(diff) - radius

    return Measurable(calculator=sphere_sdf)

def box(position, size):
    def box_sdf(pos):
        diff = np.abs(pos - position) - size
        for i in range(len(diff)):
            diff[i] = max(diff[i], 0)

        return mag(diff)

    return Measurable(calculator=box_sdf)

def plane(n, h):
    n = norm(n)
    def plane_sdf(pos):
        return np.dot(pos, n) - h
    
    return Measurable(calculator=plane_sdf)

def group(objects):
    def group_sdf(pos):
        min_sdf = float('+inf')
        for object in objects:
            sdf = object.sdf(pos)
            if sdf < min_sdf:
                min_sdf = sdf
        return min_sdf

    return Measurable(calculator=group_sdf)