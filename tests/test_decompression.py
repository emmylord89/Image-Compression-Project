import numpy as np
from src.decompression import run_length_decode, decompress_image

def test_run_length_decode():
    data = np.array([1, 2, 2, 3, 3, 1])
    decoded = run_length_decode(data)
    assert np.array_equal(decoded, np.array([1, 1, 2, 2, 2, 3]))

def test_decompress_image():
    compressed_data = b'x\x9c\x0b\xc9\xc8,V(\xcf/\xcaIQ\x04\x00)\xe4\x06\xb1'
    shape = (3, 3)
    decompressed_image = decompress_image(compressed_data, shape)
    expected_image = np.array([[1, 1, 2], [2, 2, 3], [3, 3, 3]])
    assert np.array_equal(decompressed_image, expected_image)
