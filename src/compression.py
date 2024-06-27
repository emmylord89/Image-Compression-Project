import zlib
import numpy as np

def compress_image(image_array):
    # Flatten the array before compression
    image_bytes = image_array.tobytes()
    compressed_image = zlib.compress(image_bytes)
    return compressed_image
