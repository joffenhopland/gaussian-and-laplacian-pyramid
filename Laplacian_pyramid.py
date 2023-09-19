import cv2 as cv
import numpy as np

# Load the input image
image = cv.imread("IMG_4663.JPG")

# Initialize a list to store the Gaussian pyramid levels
gpA = [image]
# Build the Gaussian pyramid with 6 levels
for i in range(5):
    image = cv.pyrDown(image)
    gpA.append(image)

# Initialize a list to store the Laplacian pyramid levels
lpA = []

# Build the Laplacian pyramid with 6 levels (biggest to smallest)
for i in range(5, 0, -1):
    size = (gpA[i - 1].shape[1], gpA[i - 1].shape[0])
    GE = cv.pyrUp(gpA[i], dstsize=size)
    L = cv.subtract(gpA[i - 1], GE)
    lpA.append(L)

# Reverse the order of Laplacian pyramid levels
print(lpA.reverse())

lpA.reverse()


# Determine the dimensions of the final image
height = sum(level.shape[0] for level in lpA)
width = max(level.shape[1] for level in lpA)

# Create a blank canvas to combine the pyramid levels
combined_image = np.zeros((height, width, 3), dtype=np.uint8)

# Initialize the vertical position
y = 0

# Paste each level of the Laplacian pyramid onto the canvas
for level in lpA:
    h, w, _ = level.shape
    combined_image[y : y + h, :w] = level
    y += h

# Save the combined Laplacian pyramid image
cv.imwrite("Laplacian.jpg", combined_image)
