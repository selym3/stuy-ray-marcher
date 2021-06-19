from .measurable import Measurable
from vec3 import Vec3
import math

'''
See shapes.py for primitive shapes
See measurable.py for operators/modifiers with constructive solid geometry
'''

def scale(primitive, s):
    ''' s is a scaling factor '''

    def scale_sdf(pos):
        return primitive.sdf(pos/s) * s
    
    return Measurable(calculator=scale_sdf)

def mod(primitive, period):
    ''' period is a vector that creates a looped space '''
    def mod_sdf(pos):
        looped = (pos % period) - (period * 0.5) 
        return primitive.sdf(looped)

    return Measurable(calculator=mod_sdf)

def mod2(primitive, px=None, py=None, pz=None):
    ''' 
    this is the same as mod but can do each dimension individually 
    (e.g. use this is in the px and pz to get a infinite plane)
    '''
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
    ''' distorter just returns a value. this might need to be paired with a 
    lower jump scale value to make more conservative marches '''

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
    ''' this can round a primitive (e.g. can round a box) '''
    def rounded_sdf(pos):
        return primitive.sdf(pos) - radius
    
    return Measurable(calculator=rounded_sdf)

def smooth_u(primitive_a, primitive_b, k=0.25):
    ''' this is a union of the two shapes, but at a distance decided by k they
    they are interpolated between '''
    def smoothu_sdf(pos):
        d1, d2 = primitive_a.sdf(pos), primitive_b.sdf(pos)
        h = max(k-abs(d1-d2), 0.0)
        return min(d1, d2) - h * h * 0.25/k

    return Measurable(calculator=smoothu_sdf)

def smooth_sub(primitive_a, primitive_b, k=0.25):
    ''' this is a subtraction of the two shapes, but at a distance decided by k they
    they are interpolated between ''' 
    def smooth_sub_sdf(pos):
        d1, d2 = primitive_a.sdf(pos), primitive_b.sdf(pos)
        h = max(k-abs(-d1-d2), 0.0)
        return max(-d2, d1) + h * h * 0.25/k

    return Measurable(calculator=smooth_sub_sdf)

def smooth_i(primitive_a, primitive_b, k=0.25):
    ''' this is an intersection of the two shapes, but at a distance decided by k they
    they are interpolated between '''
    def smooth_i_sdf(pos):
        d1, d2 = primitive_a.sdf(pos), primitive_b.sdf(pos)
        h = max(k-abs(d1-d2), 0.0)
        return max(d1, d2) + h * h * 0.25/k

    return Measurable(calculator=smooth_i_sdf)

def terraform(primitive_a, primitive_b, factor=1.0):
    ''' modifier used to terraform the surface of an
    sdf based on another sdf ''' 

    def terraform_sdf(pos):
        return primitive_a.sdf(pos) - primitive_b.sdf(pos) * factor

    return Measurable(calculator=terraform_sdf)