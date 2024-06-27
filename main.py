from src.utils import load_image, save_image
from src.compression import compress_image
from src.decompression import decompress_image
import os

# Paths
input_image_path = 'data/image.png'
compressed_image_path = 'data/compressed_image.bin'
decompressed_image_path = 'data/decompressed_image.png'

# Load the image
image_array = load_image(input_image_path)

# Compress the image
compressed_image = compress_image(image_array)

# Save compressed data
with open(compressed_image_path, 'wb') as file:
    file.write(compressed_image)

# Ensure the compressed file is not empty
if os.path.getsize(compressed_image_path) == 0:
    raise ValueError("The compressed image file is empty.")

# Decompress the image
with open(compressed_image_path, 'rb') as file:
    compressed_image = file.read()

decompressed_image_array = decompress_image(compressed_image, image_array.shape)

# Save the decompressed image
save_image(decompressed_image_array, decompressed_image_path)
