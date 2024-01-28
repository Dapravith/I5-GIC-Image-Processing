import cv2 as cv

def convert_to_grayscale(FileImage):
    height, width = FileImage.shape[:2]
    grayscale_image = FileImage.copy()

    for h in range(height):
        for w in range(width):
            R = FileImage[h][w][2]
            G = FileImage[h][w][1]
            B = FileImage[h][w][0]

            # Use the formula for Intensity RGB to Grayscale conversion Image
            intensity = 0.299 * R + 0.587 * G + 0.114 * B

            # Update the pixel value in the grayscale image
            grayscale_image[h, w] = [intensity, intensity, intensity]

    return grayscale_image

FileImage = cv.imread('./images/Test1.jpg')

# Call the function to convert the image to grayscale
New_grayScale = convert_to_grayscale(FileImage)

# Display the original and grayscale images
cv.imshow('Original image', FileImage)
cv.imshow('GrayScale image', New_grayScale)

cv.waitKey(0)
cv.destroyAllWindows()
