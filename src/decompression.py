import numpy as np
import zlib

def decompress_image(compressed_image, shape):
    """
    Decompress the image from compressed data using zlib.
    
    Parameters:
    - compressed_image: bytes, the compressed image data.
    - shape: tuple, the shape of the decompressed image.
    
    Returns:
    - np.ndarray: the decompressed image as a numpy array.
    """
    # Decompress the data
    decompressed_data = zlib.decompress(compressed_image)
    
    # Convert the decompressed data to a numpy array and reshape it
    decompressed_image = np.frombuffer(decompressed_data, dtype=np.uint8).reshape(shape)
    
    return decompressed_image
