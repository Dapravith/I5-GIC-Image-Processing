import cv2 as cv

def invert_colors(image):
    height, width, channels = image.shape
    inverted_image = image.copy()

    for h in range(height):
        for w in range(width):
            for c in range(channels):
                inverted_image[h, w, c] = 255 - image[h, w, c]

    return inverted_image

# Read the original image from file
original_image = cv.imread('./images/fruit4.jpg')

if original_image is None:
    print("Error: Could not read the original image.")
else:
    # Invert the colors
    inverted_image = invert_colors(original_image)

    # Display the original and inverted images
    cv.imshow('Original Image', original_image)
    cv.imshow('Inverted Image', inverted_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
