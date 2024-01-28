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

# Load an image from file
original_image = cv.imread('./images/fruit4.jpg')

if original_image is None:
    print("Error: Could not read the original image.")
else:
    # Display the original image
    cv.imshow('Original Image', original_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Call the function to invert the image
    inverted_image = invert_image(original_image)

    # Display the inverted image
    cv.imshow('Inverted Image', inverted_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Print the pixel values of the first few pixels in the original image
    print("Original Image Data:")
    for i in range(min(5, original_image.shape[0])):
        for j in range(min(5, original_image.shape[1])):
            print(original_image[i, j])

    # Print the pixel values of the first few pixels in the inverted image
    print("\nInverted Image Data:")
    for i in range(min(5, inverted_image.shape[0])):
        for j in range(min(5, inverted_image.shape[1])):
            print(inverted_image[i, j])
