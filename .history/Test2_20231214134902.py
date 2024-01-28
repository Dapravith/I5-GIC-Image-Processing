import cv2
import numpy as np

def convert_to_grayscale_better(image):
    if len(image.shape) == 3 and image.shape[2] == 3:  # Check if it's a BGR image
        # Extracting R, G, B channels
        blue_channel = image[:, :, 0]
        green_channel = image[:, :, 1]
        red_channel = image[:, :, 2]

        # Applying the formula: I = 0.299 * R + 0.587 * G + 0.114 * B
        grayscale_image = 0.299 * red_channel + 0.587 * green_channel + 0.114 * blue_channel

        # Convert to uint8 type (required for displaying with OpenCV)
        grayscale_image = grayscale_image.astype(np.uint8)

        return grayscale_image

    else:
        print("Input is not a BGR image.")
        return None

# Load the BGR image
image_path = './images/Test1.jpg'
bgr_image = cv2.imread(image_path)

# Convert to grayscale using the custom function
grayscale_image = convert_to_grayscale_better(bgr_image)

# Display the original and grayscale images
cv2.imshow('Original Image', bgr_image)
cv2.imshow('Grayscale Image', grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
