import cv2 as cv

def invert_image(image):
    height, width = image.shape[:2]

    for h in range(height):
        for w in range(width):
            # Invert each color channel
            B = 255 - image[h, w, 0]
            G = 255 - image[h, w, 1]
            R = 255 - image[h, w, 2]

            # Update the pixel values in the image
            image[h, w, 0] = B
            image[h, w, 1] = G
            image[h, w, 2] = R

    return image

# Load an image
imageFile = cv.imread('./images/fruit4.jpg')

# Call the function to invert the image
inverted_image = invert_image(imageFile)

# Display the original and inverted images
cv.imshow('Original Image', imageFile)
cv.imshow('Inverted Image', inverted_image)
cv.waitKey(0)
cv.destroyAllWindows()
