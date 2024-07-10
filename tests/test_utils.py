import pytest
import numpy as np
from src.utils import load_image, save_image
from PIL import Image
import os

def test_load_image():
    """Test loading an image."""
    # Create a dummy image for testing
    test_image_path = 'test_image.png'
    image_data = np.zeros((10, 10, 3), dtype=np.uint8)
    Image.fromarray(image_data).save(test_image_path)
    
    # Load the image using the function
    loaded_image = load_image(test_image_path)
    
    # Check if the loaded image matches the original data
    assert np.array_equal(loaded_image, image_data)
    
    # Clean up
    os.remove(test_image_path)

def test_save_image():
    """Test saving an image."""
    # Create a dummy image array
    test_image_array = np.zeros((10, 10, 3), dtype=np.uint8)
    test_save_path = 'saved_test_image.png'
    
    # Save the image using the function
    save_image(test_image_array, test_save_path)
    
    # Load the image back and check if it matches the original array
    loaded_image = load_image(test_save_path)
    assert np.array_equal(loaded_image, test_image_array)
    
    # Clean up
    os.remove(test_save_path)
