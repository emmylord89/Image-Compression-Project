import numpy as np
from src.decompression import run_length_decode, decompress_image

def test_run_length_decode():
    """
    Test the run-length decoding function.
    
    This test checks if the run_length_decode function correctly decodes
    a run-length encoded numpy array.
    """
    # Sample run-length encoded data
    data = np.array([1, 2, 2, 3, 3, 1])
    
    # Decode the data
    decoded = run_length_decode(data)
    
    # Expected decoded data
    expected = np.array([1, 1, 2, 2, 2, 3])
    
    # Check if the decoded data matches the expected data
    assert np.array_equal(decoded, expected)

def test_decompress_image():
    """
    Test the image decompression function.
    
    This test checks if the decompress_image function correctly decompresses
    a compressed image back to its original numpy array form.
    """
    # Sample compressed image data (using zlib compression for example)
    compressed_data = b'x\x9c\x0b\xc9\xc8,V(\xcf/\xcaIQ\x04\x00)\xe4\x06\xb1'
    
    # Expected shape of the decompressed image
    shape = (3, 3)
    
    # Decompress the image
    decompressed_image = decompress_image(compressed_data, shape)
    
    # Expected decompressed image data
    expected_image = np.array([[1, 1, 2], [2, 2, 3], [3, 3, 3]])
    
    # Check if the decompressed image matches the expected image
    assert np.array_equal(decompressed_image, expected_image)
