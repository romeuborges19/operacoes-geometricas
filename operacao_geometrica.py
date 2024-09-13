import numpy as np


class Reflexao:

    def __init__(self, image):
        self.image = np.array(image)
        self.height, self.width = self.image.shape

    def vertical_reflection(self):
        reflected_image = [
            [[0 for _ in range(self.height)] for _ in range(self.width)]
            for _ in range(self.height)
        ]

        for j in range(self.width):
            for i in range(self.height):
                reflected_image[i][j] = self.image[i][self.width - j - 1]

        return np.matrix(reflected_image)

    def horizontal_reflection(self):
        reflected_image = [
            [[0 for _ in range(self.width)] for _ in range(self.width)]
            for _ in range(self.height)
        ]

        for i in range(self.height):
            for j in range(self.width):
                reflected_image[i][j] = self.image[self.height - i - 1][j]

        return np.matrix(reflected_image)
