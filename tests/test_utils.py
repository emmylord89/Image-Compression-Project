from src.utils import load_image, save_image
import numpy as np

def test_load_image():
    image_path = 'data/example.png'
    image_array = load_image(image_path)
    assert isinstance(image_array, np.ndarray)

def test_save_image():
    image_array = np.array([[1, 1, 2], [2, 2, 3], [3, 3, 3]])
    save_image(image_array, 'data/test_image.png')
    loaded_image = load_image('data/test_image.png')
    assert np.array_equal(image_array, loaded_image)
