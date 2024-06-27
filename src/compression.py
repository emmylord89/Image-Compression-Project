import numpy as np
import zlib

def run_length_encode(data):
    encoding = []
    prev_value = data[0]
    count = 1

    for value in data[1:]:
        if value == prev_value:
            count += 1
        else:
            encoding.extend([prev_value, count])
            prev_value = value
            count = 1

    encoding.extend([prev_value, count])
    return np.array(encoding)

def compress_image(image_array):
    flattened_image = image_array.flatten()
    rle_encoded_image = run_length_encode(flattened_image)
    compressed_data = zlib.compress(rle_encoded_image.tobytes())
    return compressed_data
