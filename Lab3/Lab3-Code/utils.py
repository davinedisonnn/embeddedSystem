#File for image processing function
import numpy as np              #Importing NumPy to process matrixes
import cv2 as cv                #Importing OpenCV for image processing
import constant                 #Improting constant.py file to load all of the constant variables
from constant import center     #Importing variable center from constant.py file


def processimage(image):
    image = list(image) #Read Image Array
    image = np.array(image, np.uint8)  #Changing image array to uint8 format
    image = image.reshape(constant.res[1], constant.res[1], 3) #reshaping the array into (res,res,3) shape
    gimage = cv.cvtColor(image, cv.COLOR_RGB2GRAY) #Converting color image to Grayscale
    ret, thresh = cv.threshold(gimage, 20, 225, 0) #Finding the road inside the image
    # Calculating the centeroid using moments
    M = cv.moments(thresh)
    if M["m00"] == 0.0:
        cx = 0.0
        cy = center
    else:
        cx = float(M["m10"] / M["m00"])
        cy = float(M["m01"] / M["m00"])
    return cy