def vertical_reflection(image):
    height, width, channels = image.shape
    reflected_image = np.zeros((height, width, channels), dtype=np.uint8)
    for j in range(width):
        for i in range(height):
            reflected_image[i][j] = image[i][width - j - 1]
    return reflected_image