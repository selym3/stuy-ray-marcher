'''
Run this file with:
python main.py

Make sure GetScene is filled out properly (an example can
be used)

While rendering, the best way to quit is Escape.
After rendering, it is fine to use a force-quit or X-button.
'''

from scene import *
from marching import *
from examples import *

def GetScene():
    '''
    This function needs to return an SDF and a 
    list of light sources. See examples.py for examples of how 
    this is done or a tutorial on how to do it 
    (or return something from example.py here to see how it works)
    '''

    return Snowman()

def main():

    scene = Scene(*GetScene())

    print("Began execution...")
    
    should_render = True #<-- always render once
    while should_render:
        start = time()
        scene.execute()
        end = time()

        print(f"Took {end-start}")
        print(f"FPS: {1/(end-start)}")

        # stop rendering after first loop
        should_render = CONTINUOUS

    print("...Ended execution")
    turtle.done()

if __name__ == "__main__":
    main()
    