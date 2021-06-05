from scene import *
from marching import shapes

def main():
    z = 0
    s = 2
    scene = Scene(

        # SCENE SIZE: 
        300, 300,

        # LIGHT SOURCE:
        light = Vec3(0, 0, -1),
        
        # OBJECTS IN THE SCENE:
        objects = [
            # box(Vec3(0,0,z), Vec3(s,s,s)) - 
            # sphere(Vec3(0, 0, z), s*1.2) + 
            repeat(sphere(Vec3(0,0,z), s*0.2), period=Vec3(2,2,2))
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
    