import cv2

# Load an image
image_path = 'spider.jpg'  # Replace with the path to your image
original_image = cv2.imread(image_path)

# Check if the image is loaded successfully
if original_image is None:
    print(f"Error: Unable to load the image at {image_path}")
    exit()

# Apply Gaussian blur with a larger kernel size
kernel_size = (5, 5 )  # Adjust the kernel size as needed
blurred_image = cv2.GaussianBlur(original_image, kernel_size, 0)

# Display the original and more blurred images
cv2.imshow('Original Image', original_image)
cv2.imshow('More Blurred Image', blurred_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
