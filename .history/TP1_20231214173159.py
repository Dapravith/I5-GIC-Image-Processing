import cv2 as cv

def convert_to_grayscale(image):
    height, width = image.shape[:2]
    grayscale_image = image.copy()

    for h in range(height):
        for w in range(width):
            R = image[h, w, 2]
            G = image[h, w, 1]
            B = image[h, w, 0]

            # Use the formula for Intensity RGB to Grayscale conversion
            intensity = 0.299 * R + 0.587 * G + 0.114 * B

            # Update the pixel value in the grayscale image
            grayscale_image[h, w] = [intensity, intensity, intensity]

    return grayscale_image

image = cv.imread('./images/Test1.jpg')

# Call the function to convert the image to grayscale
grayScale = convert_to_grayscale(image)

# Display the original and grayscale images
cv.imshow('Original image', image)
cv.imshow('GrayScale image', grayScale)

cv.waitKey(0)
cv.destroyAllWindows()
