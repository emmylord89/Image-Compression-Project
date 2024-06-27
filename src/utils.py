from PIL import Image
import numpy as np

def load_image(image_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    return image_array

def save_image(image_array, output_path):
    image = Image.fromarray(image_array)
    image.save(output_path)
