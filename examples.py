'''
Scenes are made up of two things:
 - light sources
 - sdf function

Light sources is just a list of Light objects which take
in a position, color, and brightness

The sdf function can be constructed with solid geometry (can be found in marching/shapes.py)
and more complex geometries can be constructed with +,-,*,negation operators or the modifiers 
(marching/modifiers.py) which can provide cool effects on the shape or the world space itself.

Many of these are displayed in the examples (see main.py for running these examples)

It is suggested you update the constants accordingly to what the example
function might suggest in a docstring to get it to work / the best results. If no
docstring is there, the provided constants (usually fov, jump scalar, shadows and lighting are
the ones changing) should work. 

NOTE:
- Vec3 signifies an x,y,z coordinate or just a collection of 3 values 
- the parameters of each shape can be found in marching/shapes.py
'''

from marching import *

def LoopedWorld():
    ''' the constants provided work for this one, but it looks cooler with SHADOWS = True '''

    sdf = mod(sphere(Vec3(0,0,0), 0.5), 2)
    lights = [ Light(Vec3(0,0,-1), Vec3(255, 255, 255), 12) ]
    
    return sdf, lights

def Slime():
    flat = plane(Vec3(0, 1, 0), -3)
    bumps = [
        sphere(Vec3(+0, -2.5, +5), 1.5),
        sphere(Vec3(-1.5, -2.5, +6.5), 1.5),
        sphere(Vec3(+1.5, -2.5, +6.5), 1.5)
    ]

    sdf = flat
    for bump in bumps:
        sdf = smooth_u(bump, sdf, 0.75)
    
    lights = [ 
        Light(Vec3(-3,+6,-3), Vec3(0, 0, 140), 128),
        Light(Vec3(+3,+3,-6), Vec3(0, 140, 0), 156)
    
    ]

    return sdf, lights

def Snowman():
    parts = [
        sphere(Vec3(0, -1.0, 4), 1.0),
        sphere(Vec3(0, +0.2, 4), 0.7),
        sphere(Vec3(0, +1.2, 4), 0.4)
    ]

    sdf = None
    for part in parts:
        if sdf is None:
            sdf = part
        else:
            sdf = smooth_u(sdf, part, 0.35)
    
    lights = [ 
        Light(Vec3(-12, 0, -12), Vec3(255, 255, 255), 85),
        Light(Vec3(+4, 0, -4), Vec3(255, 192, 203), 120)
    ]

    return sdf, lights


def ComplexCube():
    ''' the constants provided work for this one, but it looks cooler with SHADOWS = True '''

    sdf = box(Vec3(0,0,4), 1.3) - \
        sphere(Vec3(0,0, 4), 1.75) + \
        sphere(Vec3(0, 0, 4), 0.4)

    lights = [
        Light(Vec3(6,6,-6), Vec3(8, 8, 200), 256),
        Light(Vec3(-6,6,-6), Vec3(200, 8, 8), 256)
    ]

    return sdf, lights

def Jelly():
    ''' 
    IMPORTANT: to run this one, set the JUMP_SCALAR in the constants 
    to ~0.6 for better lighting accuracy. If there are any lighting glitches, div by zero,
    or artifacts make it smaller. this one looks better with a smaller fov of 55.0
    '''

    sdf = smooth_u(
        sphere(Vec3(+1,0,5), 1.1),
        sphere(Vec3(-1,0,5), 1.1),
        0.5
    )

    def distorter(pos):
        return math.sin(5*pos.x) * \
         math.sin(5*pos.y) * \
         math.sin(5*pos.z) * \
         0.25


    sdf = distort(sdf,distorter)
    lights = [ Light(Vec3(0,0,0), Vec3(80, 80, 255), 16) ]

    return sdf, lights

def AbstractCreation():
    ''' 
    IMPORTANT: to run this one, set the JUMP_SCALAR in the constants 
    to ~0.6. If there are any lighting glitches, division by zero errors, or
    artifacts make it smaller. this one looks better with a smaller fov of 55.0
    '''

    # Distort has a default distort function (the same one as inside Jelly)
    sdf =  distort(rounded(box(Vec3(0,0,3), Vec3(0.2, 1, 0.2)), 0.1))
    lights = [ Light(Vec3(0,0,0), Vec3(80, 80, 255), 16) ]

    return sdf, lights

def EnchantedForest():
    '''
    This scene has sevaral of constants:
        - FOV - 85.0
        - POSITION - (0, -1.2, 0)
        - ANGLE - (0, 0, 12.5)
        - JUMP_SCALAR - <= 0.4
    '''

    def make_gyroid(bias, scalar, thickness):
        return rounded(scale(gyroid(bias), scalar), thickness)

    g = make_gyroid(1.3, 0.7, 0.03)
    g = terraform(g, make_gyroid(0.3, 0.11, 0.03), +0.3)
    g = g + sphere(Vec3(0, -1, 7.2), 0.5)

    lights = [ 
        Light(Vec3(0, -1, 6), Vec3(36, 200, 36), 2.0)
    ]

    return g, lights