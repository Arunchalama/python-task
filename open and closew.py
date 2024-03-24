import cv2
import numpy as np

# Load an image
image_path = 'spider.jpg'  # Change this to the path of your image
original_image = cv2.imread(image_path)

# Check if the image is loaded successfully
if original_image is None:
    print(f"Error: Unable to load the image at {image_path}")
    exit()

# Convert the image to grayscale (optional)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) #Converts a color image to a grayscale image. The Vision BGR2Gray block converts a 24-bit BGR (Blue-Green-Red). 

# Apply opening operation (erosion followed by dilation)
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8) #unsigned 8-bit integer  0 (black) to 255 (white).
opening_result = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel) #cv2.morphologyEx stands for "Extended." 

# Apply closing operation (dilation followed by erosion)
closing_result = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)

# Display the original image and the results
cv2.imshow('Original Image', original_image)
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Opening Result', opening_result)
cv2.imshow('Closing Result', closing_result)

# Wait for a key press and close the windows   




cv2.waitKey(0)
cv2.destroyAllWindows()
