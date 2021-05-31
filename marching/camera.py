class Camera:

    def __init__(self, width, height, position, angle=(0,0,0), fov=90.0):
        self.width, self.height = width, height
        
        self.position = position
        self.yaw, self.pitch, self.roll = angle
        self.fov = fov

    def generate_ray(self, pixel_x, pixel_y):
        # TODO: implement ray generation
        pass
