import cv2 as cv

image = cv.imread('./images/Pic1.jpg')

height, width = image.shape[:2]

for h in range(height):
    for w in range(width):
        B = 255 - image[h,w, 0]
        G = 255 - image[h,w, 1]
        R = 255 - image[h,w, 2]
        
        image[h,w, 0] = B
        image[h,w, 1] = G
        image[h,w, 2] = R

cv.imshow('Inversion Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
    