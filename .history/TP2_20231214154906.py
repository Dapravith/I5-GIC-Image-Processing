import cv2 as cv

imageFile = cv.imread('./images/Pic1.jpg')

height = imageFile.shape[0]
width = imageFile.shape[1]

for h in range(height):
    for w in range(width):
        B = 255 - imageFile[h,w, 0]
        G = 255 - imageFile[h,w, 1]
        R = 255 - imageFile[h,w, 2]
        
        imageFile[h,w, 0] = B
        imageFile[h,w, 1] = G
        imageFile[h,w, 2] = R
cv.imshow('Image Inversion from BGR', imageFile)
cv.waitKey(0)
cv.destroyAllWindows()