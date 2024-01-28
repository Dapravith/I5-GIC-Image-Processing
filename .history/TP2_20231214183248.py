import cv2 as cv

def invert_colors(FileImage):
    height, width = FileImage.shape[:2]
    
    for h in range(height):
        for w in range(width):
            B = 255 - FileImage[h][w][0]
            G = 255 - FileImage[h][w][1]
            R = 255 - FileImage[h][w][2]

            FileImage[h][w][0] = B
            FileImage[h][w][1] = G
            FileImage[h][w][2] = R

    return FileImage

# Read the original image from file
original_image = cv.imread('./images/fruit4.jpg')

# Check if the image is successfully loaded
if original_image is None:
    print("Error: Could not read the original image.")
else:
    # Invert the colors using the function
    inverted_image = invert_colors(original_image)

    # Display the original and inverted images
cv.imshow('Original Image', original_image)
cv.imshow('Inverted Image', inverted_image)
cv.waitKey(0)
cv.destroyAllWindows()
