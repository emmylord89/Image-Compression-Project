import zlib
import numpy as np

def decompress_image(compressed_image, shape):
    decompressed_data = zlib.decompress(compressed_image)
    decompressed_image = np.frombuffer(decompressed_data, dtype=np.uint8).reshape(shape)
    return decompressed_image
