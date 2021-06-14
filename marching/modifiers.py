from .measurable import Measurable
from vec3 import Vec3
import math

def scale(primitive, s):
    def scale_sdf(pos):
        return primitive.sdf(pos/s) * s
    
    return Measurable(calculator=scale_sdf)

def mod(primitive, period):
    def mod_sdf(pos):
        looped = (pos % period) - (period * 0.5) 
        return primitive.sdf(looped)

    return Measurable(calculator=mod_sdf)

def mod2(primitive, px=None, py=None, pz=None):
    half_period = Vec3(
        0 if px is None else px * 0.5,
        0 if py is None else py * 0.5,
        0 if pz is None else pz * 0.5
    )

    def mod2_sdf(pos):
        looped = Vec3(
            pos.x if px is None else pos.x % px,
            pos.y if py is None else pos.y % py,
            pos.z if pz is None else pos.z % pz
        ) - half_period

        return primitive.sdf(looped)

    return Measurable(calculator=mod2_sdf)

def distort(primitive, distorter=None):

    def common_distorter(pos):
        return math.sin(pos.x * 5.0) * \
             math.sin(pos.y * 5.0) * \
             math.sin(pos.z * 5.0) * 0.25

    if distorter is None:
        distorter = common_distorter

    def distortion_sdf(pos):
        return primitive.sdf(pos + distorter(pos))

    return Measurable(calculator=distortion_sdf)

def rounded(primitive, radius):
    def rounded_sdf(pos):
        return primitive.sdf(pos) - radius
    
    return Measurable(calculator=rounded_sdf)

def smooth_u(primitive_a, primitive_b, k=0.25):
    def smoothu_sdf(pos):
        d1, d2 = primitive_a.sdf(pos), primitive_b.sdf(pos)
        h = max(k-abs(d1-d2), 0.0)
        return min(d1, d2) - h * h * 0.25/k

    return Measurable(calculator=smoothu_sdf)

def smooth_sub(primitive_a, primitive_b, k=0.25):
    def smooth_sub_sdf(pos):
        d1, d2 = primitive_a.sdf(pos), primitive_b.sdf(pos)
        h = max(k-abs(-d1-d2), 0.0)
        return max(-d2, d1) + h * h * 0.25/k

    return Measurable(calculator=smooth_sub_sdf)

def smooth_i(primitive_a, primitive_b, k=0.25):
    def smooth_i_sdf(pos):
        d1, d2 = primitive_a.sdf(pos), primitive_b.sdf(pos)
        h = max(k-abs(d1-d2), 0.0)
        return max(d1, d2) + h * h * 0.25/k

    return Measurable(calculator=smooth_i_sdf)