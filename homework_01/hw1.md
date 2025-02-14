# Assignment 1 #
For the first assignment, you are required to do the following:

## Prequisites:
- A working jupyter notebook environment
- A stable Python environment with OpenCV, Matplotlib and other dependencies.

### Deadline: February 28th, 2025 11:59 PM

## Image Basics (Total Points: 13)

1. Read the image `Entlebucher.jpg` using OpenCV (Points: 1)

2. Display the original image in your notebook. You can use the function, `display_image()` from `practical1.ipynb` or create your own. Remember that OpenCV reads images as BGR and we made some modifications to the code to display it via Matplotlib. (Points: 1)

3. Once you have read the image, answer the following: (Points: 3)
    - What is the height, width and no. of channels for the image?
    - What is the total number of pixels for the image?
    - What id the pixel itensity at position x = 100, y = 110?

4. Now get the red channel for the image and display it. What do you see? and Why? [Hint: you may need to use Numpy zeros function and opencv split function] (Points: 3)

5. Now make a copy of the image and zero out the blue and green channels. Display the image now. (Points: 2)

6. Compare the images from (4) and (5) and discuss the results. (Points: 2)

7. Convert the image to grayscale and display it. (Points: 1)

## Image ROI (Points : 3)

8. Get the eye of the dog as a ROI from the original image and display it. When in doubt, follow the example shown in `practical1.ipynb`(You'll need to modify it)


## Create a random image (Points : 4)
9. Create a random RGB image (512*360) using Numpy functions [Hint: random & reshape] and display it.
10. Save the image - This is also your deliverable along with the `.ipynb` file.


## (Optional for undergrads, mandatory for graduates) [Points: 10]
11. In class we learned about the RGB color space. In your own words, write a paragraph on HSV color space, describing what each letter stands for , visualization of the color space etc. You are allowed to use online resources for this answer including commercial LLMs (as long as you cite your sources) but the write-up you submit *must* be your own words. 


## Submission Guidelines:

* Submit your code as a jupyter notebook with answers to questions written as markdown (Qs. 4, 6) and displayed on screen (Qs. 2, 3, 4, 5). You should add comments to your code at every step, especially for Qs. 9.  If you forget to do so, you won't get full score. 

**Naming convention: John_Doe_Assignment1.ipynb**

* Submit the random image you created.

**Naming convention: John_Doe_Assignment1.jpg**

* Write-up on HSV color space (for graduate students)

**Naming convention: John_Doe_Assignment1.pdf**

* Email your submissions (as a zipped file) to me. If you use github repos for submission, make sure it is not public and add me as a collaborator.

## Reference
> 1. Dog image: By Leuchtender Hund - Own work, CC BY-SA 3.0,[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=30995457)


