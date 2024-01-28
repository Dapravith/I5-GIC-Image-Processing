import cv2 as cv

def invert_colors(image):
    """
    Inverts the colors of the given image.

    Parameters:
    - image: The input image (NumPy array).

    Returns:
    - inverted_image: The image with inverted colors.
    """
    return 255 - image

def main():
    # Read the original image from file
    original_image = cv.imread('img/img1.jpg')

    if original_image is None:
        print("Error: Could not read the original image.")
        return

    # Invert the colors
    inverted_image = invert_colors(original_image)

    # Display the original and inverted images
    cv.imshow('Original Image', original_image)
    cv.imshow('Inverted Image', inverted_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
