from scene import *
from marching import shapes

if __name__ == "__main__":
    scene = Scene(

        # SCENE SIZE: 
        300, 300,

        # LIGHT SOURCE:
        light = Vec3(0, 6, 0),
        
        # OBJECTS IN THE SCENE:
        objects = [
            box(Vec3(0, 0, 6), Vec3(1, 1, 1)),
            sphere(Vec3(0, 0, 6), 1.2),

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
    