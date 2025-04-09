import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


## Function to display image using Matplotlib
def display_image(image, strng):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) ##BGR to RGB conversion for display using Matplotlib
    plt.title(strng)
    plt.imshow(image)
    plt.show()


def convolution2D(image, kernel):
    '''
    Performs 2D onvolutions on an image with a kernel.
    You are only allowed to use Numpy.
    Use appropriate padding to account for the border pixels. 
    '''


