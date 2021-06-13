from scene import *
from marching import shapes, lighting, modifiers

def main():
    y = 0
    z = 4
    s = 2

    s1, s2 = sphere(Vec3(-1.5,0,+8), 3),  sphere(Vec3(+1.5,0,+8), 1.5)

    scene = Scene(
        
        # LIGHT SOURCES
        lights = [
            Light(Vec3(6,6,-6), Vec3(8, 64, 255), 128),
            Light(Vec3(-6,6,-6), Vec3(255, 64, 8), 128)
        ],
        
        # OBJECT IN THE SCENE:
        object =
            # s1 - s2
            # smooth_sub(s1, s2, 0.50)

            smooth_sub(rounded(box(Vec3(0,y,z), 1.3), 1), sphere(Vec3(0,y,z-2),0.4), 0.5)

            # box(Vec3(0,y,z), 1.3) -
            # sphere(Vec3(0,y, z), 2.5) + 
            # sphere(Vec3(0, y, z), 0.4) + 
            # plane(Vec3(0, 1, 0), -3)

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
    