import cv2 as cv;


imageFile = cv.imread('./images/Test1.jpg');

height, width = imageFile.shape[0]
height, width = imageFile.shape[1]
height, width = imageFile.shape[2]


for h in range(height) :
    for w in range(width) :
        B = imageFile[h,w]
        G = imageFile[h,w]
        R = imageFile[h,w]
        # Use RGB's Formula RGB = 0.299*R + 0.587*G + 0.114*B
        imageFile[h,w] = 0.114*B + 0.587*G + 0.299*R
cv.imshow('OrignalScale', imageFile)
cv.imshow('GrayScale', imageFile)
cv.waitKey(0)        


