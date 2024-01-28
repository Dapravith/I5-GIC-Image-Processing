import cv2
import numpy as np

def convert_image(image_path):
    original_image = cv2.imread(image_path)
    h, w, _ = original_image.shape
    hw = w // 2
    hh = h // 2

    top_left = original_image[:hh, :hw]
    top_right = np.zeros_like(top_left)
    top_right[:, :, 2] = original_image[:hh, hw:, 2]
    bottom_left = np.zeros_like(top_left)
    bottom_left[:, :, 1] = original_image[hh:, :hw, 1]
    bottom_right = np.zeros_like(top_left)
    bottom_right[:, :, 0] = original_image[hh:, hw:, 0]

    result_image = np.concatenate((top_left, top_right, bottom_left, bottom_right), axis=1)

    return result_image

# Example usage
input_image_path = './images/Pic1.jpg';
output_image = convert_image(input_image_path)

cv2.imshow('Original Images', cv2.imread(input_image_path))
cv2.imshow('Modified Images', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
