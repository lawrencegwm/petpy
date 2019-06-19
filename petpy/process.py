"""
Processing Utilities
"""
import numpy as np


def smooth_curve(curve, length):
    """
    Smooth a curve with a boxcar of length n elements
    """
    boxcar = np.ones(length) / length
    return np.convolve(boxcar, curve, mode="same")
