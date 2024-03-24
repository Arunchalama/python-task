import cv2
import numpy as np

img = cv2.imread('sun.jpg')
#add the pixel dilation
#remove the pixel erosion

# Check if the image is loaded successfully
if img is None:
    print("Error: Image not loaded.")
else:
    # Display the input image
    cv2.imshow('Input Image', img)

    # Define the kernel for erosion and dilation 
    #kernel also known as a structuring element)
    kernel = np.ones((5, 5), np.uint8)  #8bit range 0 to 255
   #np.ones is a function from the NumPy library in Python, and it is used to create an array or matrix filled with ones.
    # Perform erosion
    img_erosion = cv2.erode(img, kernel, iterations=2)
    cv2.imshow('Erosion', img_erosion)

    # Perform dilation
    img_dilation = cv2.dilate(img, kernel, iterations=2)
    cv2.imshow('Dilation', img_dilation)

    # Wait for a key event and close all windows if 'w' is pressed
    if cv2.waitKey(0) & 0xFF == ord('w'):
        cv2.destroyAllWindows()
