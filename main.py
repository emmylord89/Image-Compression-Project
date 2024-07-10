import os
import numpy as np
from src.utils import load_image, save_image
from src.compression import compress_image
from src.decompression import decompress_image

# Load the image
image_path = 'data/image.png'
image_array = load_image(image_path)

# Compress the image
compressed_image = compress_image(image_array)

# Save compressed data
compressed_path = 'data/compressed_image.bin'
with open(compressed_path, 'wb') as file:
    file.write(compressed_image)

# Read the compressed data back
with open(compressed_path, 'rb') as file:
    compressed_image = file.read()

# Decompress the image
decompressed_image_array = decompress_image(compressed_image, image_array.shape)

# Save the decompressed image
save_image(decompressed_image_array, 'data/decompressed_image.png')
