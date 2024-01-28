import cv2 as cv
import numpy as np

img = cv.imread("images/fruit3.jpg")

def adjust_brightness_darkness(image, change):
    # Ensuring the values are between 0 and 255
    new_image = np.clip(image + change, 0, 255).astype(np.uint8)
    return new_image

# Adjust brightness and darkness
brightness_adjusted = adjust_brightness_darkness(img, 100)  # increase by 200 for brightness
darkness_adjusted = adjust_brightness_darkness(img, -100)  # decrease by 200 for darkness

# Display images
cv.imshow("Original Image", img)
cv.imshow("Brightness Image", brightness_adjusted)
cv.imshow("Darkness Image", darkness_adjusted)

cv.waitKey(0)
cv.destroyAllWindows()
