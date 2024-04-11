import numpy as np

def bukin_2d(x, y):
    """
    Bukin function in 2D.

    Parameters:
        x (float): The x-coordinate.
        y (float): The y-coordinate.

    Returns:
        float: The value of the Bukin function at the given point.
    """
    return 100 * np.sqrt(np.abs(y - 0.01 * x**2)) + 0.01 * np.abs(x + 10)


init_ranges = ((-15, -5), (-3, 3))
