import cv2 as cv;
import numpy as np

# Load the image
img = cv2.imread('images/fruit3.jpg')

# Ensure img is not empty
if img is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width, _ = img.shape

# Initialize histograms and LUTs for each color channel
histoB = np.zeros(256, np.int)
histoG = np.zeros(256, np.int)
histoR = np.zeros(256, np.int)
LUTB = np.zeros(256)
LUTG = np.zeros(256)
LUTR = np.zeros(256)

# Calculate the histogram for each color channel
for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]
        histoB[b] += 1
        histoG[g] += 1
        histoR[r] += 1

# Calculate the cumulative histogram (cumulative distribution function)
for i in range(1, 256):
    histoB[i] += histoB[i - 1]
    histoG[i] += histoG[i - 1]
    histoR[i] += histoR[i - 1]

# Normalize the histograms and calculate LUT
total_pixels = width * height
LUTB = (histoB / total_pixels) * 255
LUTG = (histoG / total_pixels) * 255
LUTR = (histoR / total_pixels) * 255

# Apply histogram equalization
equalized_img = np.zeros_like(img)
for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]
        equalized_img[i, j, 0] = LUTB[b]
        equalized_img[i, j, 1] = LUTG[g]
        equalized_img[i, j, 2] = LUTR[r]

# Display the original and equalized images
cv2.imshow('Original', img)
cv2.imshow('Histogram Equalized', equalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
