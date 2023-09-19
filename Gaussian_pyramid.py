import cv2 as cv
import numpy as np

# Load the input image
image = cv.imread("IMG_4663.JPG")

# Initialize a list to store the pyramid levels
pyramid = [image]

# Build the Gaussian pyramid with 6 levels
for i in range(5):
    image = cv.pyrDown(image)
    pyramid.append(image)

# Determine the dimensions of the final image
height = sum(level.shape[0] for level in pyramid)
width = max(level.shape[1] for level in pyramid)

# Create a blank canvas to combine the pyramid levels
combined_image = np.zeros((height, width, 3), dtype=np.uint8)

# Initialize the vertical position
y = 0

# Paste each level of the pyramid onto the canvas
for level in pyramid:
    h, w, _ = level.shape
    combined_image[y : y + h, :w] = level
    y += h

# Save the combined image
cv.imwrite("Gaussian.jpg", combined_image)
