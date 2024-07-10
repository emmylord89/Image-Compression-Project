import pytest
import numpy as np
from src.compression import compress_image, decompress_image
from PIL import Image

def test_compress_image():
    """Test compressing an image."""
    # Create a dummy image array
    image_array = np.zeros((10, 10, 3), dtype=np.uint8)
    
    # Compress the image using the function
    compressed_image = compress_image(image_array, quality=85)
    
    # Check if the result is in byte format
    assert isinstance(compressed_image, bytes)

def test_decompress_image():
    """Test decompressing an image."""
    # Create a dummy image array
    original_array = np.zeros((10, 10, 3), dtype=np.uint8)
    
    # Compress the image to get compressed data
    compressed_image = compress_image(original_array, quality=85)
    
    # Decompress the image back to numpy array
    decompressed_image = decompress_image(compressed_image, original_array.shape)
    
    # Check if the decompressed image matches the original array
    assert decompressed_image.shape == original_array.shape
    assert isinstance(decompressed_image, np.ndarray)
