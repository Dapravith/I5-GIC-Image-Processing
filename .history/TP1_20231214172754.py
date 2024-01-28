import cv2 as cv

def ConvertColor2Gray(image, channel=0):
    if channel not in {0, 1, 2}:
        print("Invalid channel value. Please choose 0 (Blue), 1 (Green), or 2 (Red).")
        return None

    def calculate_intensity(pixel):
        return int(0.114 * pixel[0] + 0.587 * pixel[1] + 0.299 * pixel[2])

    h, w, c = image.shape

    # Create an empty grayscale image
    grayscale_image = [[[0, 0, 0] for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            # Calculate intensity for the specified color channel
            intensity = calculate_intensity([image[i, j, 0], image[i, j, 1], image[i, j, 2]])
            # Set intensity as the value for all three channels
            grayscale_image[i][j][channel] = intensity

    return grayscale_image

img = cv.imread('color-picker.png')

# Call the function to convert the image to grayscale for a specific color channel
gray_image = ConvertColor2Gray(img, channel=1)  # Change the channel value (0 for Blue, 1 for Green, 2 for Red)

# Display the original and grayscale images
cv.imshow("Grayscale Image", gray_image)
cv.imshow("Original Image", img)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()
