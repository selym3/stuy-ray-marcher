from scene import *
from marching import shapes

def main():
    scene = Scene(

        # SCENE SIZE: 
        100, 100,

        # LIGHT SOURCE:
        light = Vec3(0, 0, -6),
        
        # OBJECTS IN THE SCENE:
        objects = [
            box(Vec3(0, 0, 6), Vec3(1, 1, 1)) - 
            sphere(Vec3(0, 0, 6), 1.5), 

            plane(Vec3(0,1,0), -3),
        ]
        
    )

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
    