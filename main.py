import cv2
import numpy as np


def build_gaussian_pyramid(image, levels):
    pyramid = [image]
    for i in range(levels - 1):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid


def build_laplacian_pyramid(gaussian_pyramid, levels):
    pyramid = []
    for i in range(5, 0, -1):
        size = (gaussian_pyramid[i - 1].shape[1], gaussian_pyramid[i - 1].shape[0])
        GE = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
        L = cv2.subtract(gaussian_pyramid[i - 1], GE)
        pyramid.append(L)
    pyramid.reverse()
    return pyramid


def visualize_pyramid(pyramid, title):
    height = sum(level.shape[0] for level in pyramid)
    width = max(level.shape[1] for level in pyramid)
    combined_image = np.zeros((height, width, 3), dtype=np.uint8)
    y = 0

    for level in pyramid:
        h, w, _ = level.shape
        combined_image[y : y + h, :w] = level
        y += h
    cv2.imwrite(title, combined_image)
    cv2.imshow(title, combined_image)
    cv2.waitKey(0)


def main():
    img = cv2.imread("IMG_4663.JPG")
    levels = 6

    gaussian_pyramid = build_gaussian_pyramid(img, levels)
    laplacian_pyramid = build_laplacian_pyramid(gaussian_pyramid, levels)

    # comment and uncomment depending on which one you want to visualize
    visualize_pyramid(gaussian_pyramid, "Gaussian.jpg")
    visualize_pyramid(laplacian_pyramid, "Laplacian.jpg")


if __name__ == "__main__":
    main()
