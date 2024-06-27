import numpy as np
import zlib

def run_length_decode(data):
    decoded = []
    for i in range(0, len(data), 2):
        value = data[i]
        count = data[i + 1]
        decoded.extend([value] * count)
    return np.array(decoded)

def decompress_image(compressed_data, shape):
    decompressed_data = zlib.decompress(compressed_data)
    decompressed_rle_image = np.frombuffer(decompressed_data, dtype=np.uint8)
    decompressed_image_data = run_length_decode(decompressed_rle_image)
    decompressed_image_array = decompressed_image_data.reshape(shape)
    return decompressed_image_array
