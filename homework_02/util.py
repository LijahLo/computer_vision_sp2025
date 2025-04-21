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
    # Convert to grayscale if color is RGB(3D)
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    image = image.astype(np.float32)  # Ensure float for accurate computation
    kernel = np.flipud(np.fliplr(kernel))  # Flip the kernel for convolution

    # Get dimensions
    iH, iW = image.shape
    kH, kW = kernel.shape
    pad_h, pad_w = kH // 2, kW // 2

    # Pad the image with zeros
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    # Create an output image
    output = np.zeros_like(image)

    # Perform convolution
    for y in range(iH):
        for x in range(iW):
            region = padded_image[y:y+kH, x:x+kW]
            output[y, x] = np.sum(region * kernel)

    # Normalize to range [0, 255]
    output = np.clip(output, 0, 255)
    return output.astype(np.uint8)
