from scene import *

if __name__ == "__main__":
    scene = Scene(300, 300)

    print("Began execution...")

    while scene.is_running():
        start = time()
        scene.execute()
        end = time()

        print(f"Took {end-start}")
        print(f"FPS: {1/(end-start)}")

    print("...Ended execution")
    