def SceneSdf(pos, objects):
    ''' 
    For an entire scene (highest level), the SDF is the 
    minimum of all the measurable objects so that the ray
    marches properly.
    '''

    min_sdf = float('+inf')
    for object in objects:
        sdf = object.sdf(pos)
        if sdf < min_sdf:
            min_sdf = sdf
    
    return min_sdf

def MarchRay(ray, objects):
    # TODO: implement marching
    return (0, 0, 0)