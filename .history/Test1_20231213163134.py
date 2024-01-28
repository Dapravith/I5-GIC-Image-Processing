import cv2
import numpy as np

def convert_image(image_path):
    # Load the original image
    original_image = cv2.imread(image_path)

    # Split the image into four parts
    height, width, _ = original_image.shape
    half_width = width // 2
    half_height = height // 2

    # Top-left: original color
    top_left = original_image[:half_height, :half_width]

    # Top-right: no red and green components
    top_right = original_image[:half_height, half_width:]
    top_right[:, :, 0] = 0  # Set red channel to 0
    top_right[:, :, 1] = 0  # Set green channel to 0

    # Bottom-left: no red and blue components
    bottom_left = original_image[half_height:, :half_width]
    bottom_left[:, :, 0] = 0  # Set red channel to 0
    bottom_left[:, :, 2] = 0  # Set blue channel to 0

    # Bottom-right: no green and blue components
    bottom_right = original_image[half_height:, half_width:]
    bottom_right[:, :, 1] = 0  # Set green channel to 0
    bottom_right[:, :, 2] = 0  # Set blue channel to 0

    # Concatenate the four parts to get the final image
    result_image = np.concatenate((top_left, top_right, bottom_left, bottom_right), axis=1)

    return result_image

# Example usage
input_image_path = 'path_to_your_image.jpg'
output_image = convert_image(input_image_path)

# Display the original and modified images
cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('Modified Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
