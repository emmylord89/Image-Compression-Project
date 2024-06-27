from src.utils import load_image, save_image
from src.compression.py import compress_image
from src.decompression.py import decompress_image

# Load the image
image_path = 'data/example.png'
image_array = load_image(image_path)

# Compress the image
compressed_image = compress_image(image_array)

# Save compressed data
with open('data/compressed_image.bin', 'wb') as file:
    file.write(compressed_image)

# Decompress the image
with open('data/compressed_image.bin', 'rb') as file:
    compressed_image = file.read()

decompressed_image_array = decompress_image(compressed_image, image_array.shape)

# Save the decompressed image
save_image(decompressed_image_array, 'data/decompressed_image.png')
