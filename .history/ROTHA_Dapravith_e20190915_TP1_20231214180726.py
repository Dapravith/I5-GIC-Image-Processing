import cv2 as cv

# Function to convert an color image to grayscale
def convert_to_grayscale_image(FileImage):
    # Get the height, width value of the image
    height = FileImage.shape[:2]
    width = FileImage.shape[:2]
    # Create a copy of the original image to store the grayscale version
    grayscale_image = FileImage.copy()
    # Use for loop condition each pixel in the color channel image
    for h in range(height):
        for w in range(width):
            R = FileImage[h][w][2]
            G = FileImage[h][w][1]
            B = FileImage[h][w][0]

            # Apply the formula for Intensity RGB equation to Grayscale conversion Image
            intensity_RGB = 0.299 * R + 0.587 * G + 0.114 * B

            # Update the pixel value in the grayscale image
            grayscale_image[h][w] = [intensity_RGB] * 3

    return grayscale_image

# Read the orignal color image
FileImage = cv.imread('./images/fruit1.jpg')

# Call the function to convert the image to GrayScale
New_grayScale = convert_to_grayscale_image(FileImage)

# Display the original and grayscale images
cv.imshow('OriginalScale Image', FileImage)
cv.imshow('GrayScale Image', New_grayScale)

# Wait for the key event then close the windows of image
cv.waitKey(0)
cv.destroyAllWindows()
