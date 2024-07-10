import numpy as np
from PIL import Image

def load_image(image_path):
    """
    Load an image from a file and return as a numpy array.
    
    Parameters:
    - image_path: str, path to the image file.
    
    Returns:
    - np.ndarray: image as a numpy array.
    """
    image = Image.open(image_path)
    return np.array(image)

def save_image(image_array, image_path):
    """
    Save a numpy array as an image file.
    
    Parameters:
    - image_array: np.ndarray, the image data to save.
    - image_path: str, path where the image will be saved.
    """
    image = Image.fromarray(image_array)
    image.save(image_path)
