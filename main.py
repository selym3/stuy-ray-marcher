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

    return ComplexCube()

def main():

    scene = Scene(*GetScene())

    print("Began execution...")
 
    while scene.is_running():
        start = time()
        scene.execute()
        end = time()

        print(f"Took {end-start}")
        print(f"FPS: {1/(end-start)}")

    print("...Ended execution")

if __name__ == "__main__":
    main()
    