import cv2 as cv

image = cv.imread('./images/Test1.jpg')

# Get the height and width of the image
height = image.shape[0]
width = image.shape[1]

# Create an empty grayscale image
grayScale = image.copy()

# Loop through each pixel and convert to grayscale
for h in range(height):
    for w in range(width):
        B = image[h, w, 2]
        G = image[h, w, 1]
        R = image[h, w, 0]

        # Use the formula for Intensity RGB to Grayscale conversion
        IntensityToGrayScale = 0.299 * R + 0.587 * G + 0.114 * B

        # Update the pixel value in the grayscale image
        grayScale[h, w] = [IntensityToGrayScale, IntensityToGrayScale, IntensityToGrayScale]

# Display the original and grayscale images
cv.imshow('Original image', image)
cv.imshow('GrayScale image', grayScale)

cv.waitKey(0)
cv.destroyAllWindows()
