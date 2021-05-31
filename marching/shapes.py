from .measurable import Measurable
import numpy as np
from utils import mag

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
