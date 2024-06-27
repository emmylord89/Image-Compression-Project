
### `tests/test_compression.py`

```python
import numpy as np
from src.compression import run_length_encode, compress_image

def test_run_length_encode():
    data = np.array([1, 1, 2, 2, 2, 3])
    encoded = run_length_encode(data)
    assert np.array_equal(encoded, np.array([1, 2, 2, 3, 3, 1]))

def test_compress_image():
    image_array = np.array([[1, 1, 2], [2, 2, 3], [3, 3, 3]])
    compressed = compress_image(image_array)
    assert compressed is not None
