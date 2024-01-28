import cv2 as cv

def convert_to_grayscale(image):
    if len(image.shape) == 3 and image.shape[2] == 3:  # Check if it's a color image (3 channels)
        # Get the height and width of the image
        height = image.shape[0]
        width = image.shape[1]

        # Create an empty grayscale image
        grayscale_image = [[0] * width for _ in range(height)]

        # Loop through each pixel and convert to grayscale
        for h in range(height):
            for w in range(width):
                B = image[h, w, 0]
                G = image[h, w, 1]
                R = image[h, w, 2]

                # Calculate the grayscale value using the luminance formula
                grayscale_image[h][w] = int(0.299 * R + 0.587 * G + 0.114 * B)

        return grayscale_image
    else:
        print("Input is not a color image.")
        return None

# Load a color image
image_path = './images/Test1.jpg'
color_image = cv.imread(image_path)

# Convert to grayscale using the custom function
grayscale_image = convert_to_grayscale(color_image)

# Display the original color and grayscale images
cv.imshow('Original Color Image', color_image)
cv.imshow('Grayscale Image', grayscale_image)
cv.waitKey(0)
cv.destroyAllWindows()
