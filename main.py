from scene import *
from marching import shapes

def main():
    z = 0
    scene = Scene(

        # SCENE SIZE: 
        300, 300,

        # LIGHT SOURCE:
        light = Vec3(0, 0, -1),
        
        # OBJECTS IN THE SCENE:
        objects = [
            repeat(
                primitive=box(Vec3(0,0,z), Vec3(0.4, 0.4, 0.4)) - sphere(Vec3(0, 0, z), 0.5) + sphere(Vec3(0,0,z), 0.1),
                period=Vec3(2,2,2)
            )
            # plane(Vec3(0, 1, 0), -3)
        ]
        
    )

    print("Began execution...")
 
    while scene.is_running():
        start = time()
        scene.execute_multi(thread_count=16)
        end = time()

        print(f"Took {end-start}")
        print(f"FPS: {1/(end-start)}")

    print("...Ended execution")

if __name__ == "__main__":
    main()
    