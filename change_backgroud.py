import ctypes
import cv2
import os
import resize
import tempfile
import numpy as np


def set_wallpaper(img):

    #if 'frame' in img: 
      #img = cv2.imread(img)
      #img = resize.resized(img)   

    # Set wallpaper using the temporary file path
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)
