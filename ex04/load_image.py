from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image file and return its pixel data as numpy array

    Args:
        path: Path to the image file

    Returns:
        numpy.ndarray: RGB pixel data
    """
    try:
        # Attempt to load the image
        with Image.open(path) as img:
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Convert to numpy array
            array = np.array(img)

            # Print shape information
            print(f"The shape of image is: {array.shape}")

            return array

    except FileNotFoundError:
        raise ValueError(f"Error: File '{path}' not found")
    except (IOError, OSError):
        raise ValueError(f"Error: Unable to load image '{path}'")
    except Exception as e:
        raise ValueError(f"Error: Unexpected error loading '{path}': {str(e)}")
