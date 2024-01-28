import cv2 as cv

img = cv.imread("images/fruit3.jpg")
cv.imshow("Original Image", img)

def adjust_darkness(image, modify_value):
    darkness = image.copy()
    for x in range(len(image)):
        for y in range(len(image[x])):
            for c in range(3):  # Loop through color channels
                darkness[x, y, c] = max(image[x, y, c] - modify_value, -255)
    return darkness

def adjust_brightness(image, modify_value):
    brightness = image.copy()
    for x in range(len(image)):
        for y in range(len(image[x])):
            for c in range(3):  # Loop through color channels
                brightness[x, y, c] = min(image[x, y, c] + modify_value, 255)
    return brightness

# Apply adjustments
darkness_image = adjust_darkness(img, 80)
brightness_image = adjust_brightness(img, 100)

# Display results
cv.imshow("Darkness Image", darkness_image)
cv.imshow("Brightness Image", brightness_image)

cv.waitKey(0)
cv.destroyAllWindows()
