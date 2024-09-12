def vertical_reflection(image):
    height, width, channels = image.shape
    reflected_image = np.zeros((height, width, channels), dtype=np.uint8)
    for j in range(width):
        reflected_image[:, j] = image[:, width - j - 1]
    return reflected_image