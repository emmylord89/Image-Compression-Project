import numpy as np
from PIL import Image

def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

def save_image(image_array, save_path):
    image = Image.fromarray(image_array)
    image.save(save_path)
