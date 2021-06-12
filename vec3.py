USE_CPP = False

if USE_CPP:
    import linalg
    Vec3 = linalg.Vec3
else:
    import pyvec3
    Vec3 = pyvec3.Vec3