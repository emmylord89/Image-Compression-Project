import numpy as np
import zlib

def compress_image(image_array):
    """
    Compress the image array using zlib compression.
    
    Parameters:
    - image_array: np.ndarray, the image data to compress.
    
    Returns:
    - bytes: compressed image in byte format.
    """
    # Convert the numpy array to bytes
    image_data = image_array.tobytes()
    
    # Compress the image data
    compressed_image = zlib.compress(image_data)
    
    return compressed_image
