from scene import *
from marching import shapes, lighting

def main():
    y = 1.2
    z = 6
    s = 2

    scene = Scene(
        
        # LIGHT SOURCES
        lights = [
            Light(Vec3(6,6,-6), Vec3(8, 64, 255), 128),
            Light(Vec3(-6,6,-6), Vec3(255, 64, 8), 128),
            Light(Vec3(0,0,-120), Vec3(255,255,255), 256)
        ],
        
        # OBJECT IN THE SCENE:
        object = 
            box(Vec3(0,y,z), s) -
            sphere(Vec3(0,y, z), s*1.2) + 
            sphere(Vec3(0, y, z), s*0.2) + 
            plane(Vec3(0, 1, 0), -3)

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
    