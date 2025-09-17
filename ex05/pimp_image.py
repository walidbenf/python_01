import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    # Utilise uniquement =, +, -, *
    result = array * 0 + 255 - array
    plt.imshow(result)
    plt.title("Inverted")
    plt.show()
    return result

def ft_red(array):
    """
    Keeps only the red channel of the image.
    """
    # Utilise uniquement =, *
    result = array * 1
    result[..., 1] = 0 * result[..., 1]
    result[..., 2] = 0 * result[..., 2]
    plt.imshow(result)
    plt.title("Red filter")
    plt.show()
    return result

def ft_green(array):
    """
    Keeps only the green channel of the image.
    """
    # Utilise uniquement =, -
    result = array - array
    result[..., 1] = array[..., 1]
    plt.imshow(result)
    plt.title("Green filter")
    plt.show()
    return result

def ft_blue(array):
    """
    Keeps only the blue channel of the image.
    """
    # Utilise uniquement =
    result = array * 0
    result[..., 2] = array[..., 2]
    plt.imshow(result)
    plt.title("Blue filter")
    plt.show()
    return result

def ft_grey(array):
    """
    Converts the image to greyscale.
    """
    # Utilise uniquement =, /
    grey = (array[..., 0] / 3 + array[..., 1] / 3 + array[..., 2] / 3).astype(np.uint8)
    result = np.zeros_like(array)
    result[..., 0] = grey
    result[..., 1] = grey
    result[..., 2] = grey
    plt.imshow(result)
    plt.title("Grey filter")
    plt.show()
    return result