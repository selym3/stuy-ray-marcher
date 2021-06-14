'''
Constants stores most of the numbers that may be relevant to change / update
but will not often be changed when designing a scene. 
'''

'''
The size of the turtle window / the area of the turtle
window in which rendering takes place (in pixels)
'''
WIDTH = 1024
HEIGHT = 1024

'''
The amount of pixels that will have a color calculated. These will
be packed into the width , height. The resolution can larger
than or greater than the real width, height. 
'''
RESOLUTION = (512, 512)

'''
A string that is the path to an image. The current frame will 
be saved inside of it. If this is False/None/ not a string it 
will not save
'''
SAVE_AS = None # 'images/jelly.png'

'''
These are configuration options for the camera.

The fov is the field of view in degrees. The angle is where
the camera is looking in degrees. The position is an x,y,z coordinate.
'''
FOV = 90.0
POSITION = (0, 0, 0)
ANGLE = (0, 0, 0)

'''
These are threading options. 

Threads is the number of threads in the threadpool. Animate fill will render 
the progress of a frame before it is finished, otherwise you will have to wait with a blank screen. The effect is enhanced by a greater/prime
number of threads.

The threads mean less on Windows because the multiprocessing library didn't work the same on 
windows as it did on Linux.
'''
THREADS = 17
ANIMATE_FILL = True

'''
These are the ray marching configurations.

Max steps is the max number of jumps a ray can make regardless of distance
marched. Max distance sets a cap on the distance a ray can travel. Surface distance
is the max distance away a ray can be from a surface before it is registered as a hit.
'''
MAX_STEPS = 128
MAX_DISTANCE = 64
SURFACE_DISTANCE = 0.01

'''
These are the lighting configuration options.

These parameters are described in: https://en.wikipedia.org/wiki/Phong_reflection_model

Phong lighting doesn't take into account shadows by default, it's often added on, so it can be 
turned off.
'''

SPECULAR = 0.3
DIFFUSE = 1
AMBIENT = 0.01
SHININESS = 96

SHADOWS = False

'''
If camera movement, animation, or anything that necessitates multiple
frames is added, it is necessary to turn on continuous mode
'''
CONTINUOUS = False