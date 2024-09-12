class Reflexao:


    def __init__(self, image):
        self.image = image

    def vertical_reflection(self):
        height, width, channels = self.image.shape
        
        reflected_image = [[[0 for _ in range(channels)] for _ in range(width)] for _ in range(height)]
        
        for j in range(width):
                reflected_image[:, j] = self.image[:, width - j - 1]    
         
        return reflected_image

