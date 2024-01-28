import cv2
import numpy as np

def transform_image(image):
    # Get image dimensions
    height, width, channels = image.shape

    # Split the image into four parts
    top_left = image[:height//2, :width//2].copy()
    top_right = image[:height//2, width//2:].copy()
    bottom_left = image[height//2:, :width//2].copy()
    bottom_right = image[height//2:, width//2:].copy()

    # Top-right: No red and green components
    top_right[:, :, 0] = 0  # Set red channel to zero
    top_right[:, :, 1] = 0  # Set green channel to zero

    # Bottom-left: No red and blue components
    bottom_left[:, :, 0] = 0  # Set red channel to zero
    bottom_left[:, :, 2] = 0  # Set blue channel to zero

    # Bottom-right: No green and blue components
    bottom_right[:, :, 1] = 0  # Set green channel to zero
    bottom_right[:, :, 2] = 0  # Set blue channel to zero

    # Concatenate the modified parts to form the transformed image
    transformed_image = np.concatenate([top_left, top_right, bottom_left, bottom_right], axis=1)

    return transformed_image

# Example usage
# Load the original image using OpenCV
original_image = cv2.imread('path_to_your_image.jpg')

# Convert to the desired format
transformed_image = transform_image(original_image)

# Display the original and transformed images
cv2.imshow('Original Image', original_image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
