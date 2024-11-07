import ctypes
import numpy as np


def set_wallpaper(img):

    # Set wallpaper using the temporary file path
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)
