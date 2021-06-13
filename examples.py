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

'''

from marching import *

def LoopedWorld():
    sdf = mod(sphere(Vec3(0,0,0), 0.5), 2)
    lights = [ Light(Vec3(0,0,-1), Vec3(255, 255, 255), 12) ]
    
    return sdf, lights

def BumpInTheRoad():
    sdf = smooth_u(
        sphere(Vec3(0,-2.5,+6), 1.5),
        plane(Vec3(0,1,0), -3),
        0.75
    )

    lights = [ Light(Vec3(0,6,-3), Vec3(0, 0, 200), 128) ]

    return sdf, lights

def ComplexCube():
    sdf = box(Vec3(0,0,4), 1.3) - \
        sphere(Vec3(0,0, 4), 1.75) + \
        sphere(Vec3(0, 0, 4), 0.4)

    lights = [
        Light(Vec3(6,6,-6), Vec3(8, 64, 140), 256),
        Light(Vec3(-6,6,-6), Vec3(140, 64, 8), 256)
    ]

    return sdf, lights