import cv2 as cv

def ConvertColor2Gray(image):
    h, w, c = image.shape
    
    # Create an empty grayscale image
    gray_image = [[[0, 0, 0] for _ in range(w)] for _ in range(h)]

    for x in range(h):
        for y in range(w):
            # Extract individual color channels
            b = image[x, y, 0]
            g = image[x, y, 1]
            r = image[x, y, 2]

            # Calculate grayscale value using the formula: (0.114*b) + (0.587*g) + (0.299*r)
            intensity = int(0.114 * b + 0.587 * g + 0.299 * r)

            # Set intensity as the value for all three channels
            gray_image[x][y] = [intensity, intensity, intensity]
    
    return gray_image

img = cv.imread('./images/Pic1.jpg')

# Call the function to convert the image to grayscale
gray_image = ConvertColor2Gray(img)

# Display the original and grayscale images
cv.imshow("Grayscale Image", gray_image)
cv.imshow("Original Image", img)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()
