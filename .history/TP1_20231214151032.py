import cv2

image = cv2.imread('./images/Test1.jpg')

# Get the height and width of the image
height, width = image.shape[:2]

# Create an empty grayscale image
gray = image.copy()

# Loop through each pixel and convert to grayscale
for h in range(height):
    for w in range(width):
        B = image[h, w, 0]
        G = image[h, w, 1]
        R = image[h, w, 2]

        # Use the formula for RGB to Grayscale conversion
        new_gray_value = 0.299 * R + 0.587 * G + 0.114 * B

        # Update the pixel value in the grayscale image
        gray[h, w] = [new_gray_value, new_gray_value, new_gray_value]

# Display the original and grayscale images
cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
