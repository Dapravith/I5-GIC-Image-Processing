import cv2 as cv
import numpy as np

img = cv.imread("images/fruit3.jpg")
cv.imshow("Original Image", img)

def adjust_darkness(image, modify_value):
    # Ensure values are within [0, 255]
    darkness = np.maximum(image - modify_value, 0).astype(np.uint8)
    return darkness

def adjust_brightness(image, modify_value):
    # Ensure values are within [0, 255]
    brightness = np.minimum(image + modify_value, 255).astype(np.uint8)
    return brightness

# Apply adjustments
darkness_image = adjust_darkness(img, - 150)
brightness_image = adjust_brightness(img, 150)

# Display results
cv.imshow("Darkness Image", darkness_image)
cv.imshow("Brightness Image", brightness_image)

cv.waitKey(0)
cv.destroyAllWindows()
