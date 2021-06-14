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

NOTE:
- Vec3 signifies an x,y,z coordinate or just a collection of 3 values 
- the parameters of each shape can be found in marching/shapes.py
'''

from marching import *

def LoopedWorld():
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
    sdf = box(Vec3(0,0,4), 1.3) - \
        sphere(Vec3(0,0, 4), 1.75) + \
        sphere(Vec3(0, 0, 4), 0.4)

    lights = [
        Light(Vec3(6,6,-6), Vec3(8, 8, 200), 256),
        Light(Vec3(-6,6,-6), Vec3(200, 8, 8), 256)
    ]

    return sdf, lights

def Jelly():

    def distorter(pos):
        return math.sin(5*pos.x) * \
         math.sin(5*pos.y) * \
         math.sin(5*pos.z) * \
         0.25

    sdf = distort(
        smooth_u(
            sphere(Vec3(+1,0,3), 1.1),
            sphere(Vec3(-1,0,3), 1.1),
            0.5
        ), 
        distorter
    )

    lights = [ Light(Vec3(-1,0,-3), Vec3(255, 45, 10), 128) ]

    return sdf, lights
