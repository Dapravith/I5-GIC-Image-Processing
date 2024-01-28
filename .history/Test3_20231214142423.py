import cv2 as cv

imagePhoto = cv.imread('./images/Pic1.jpg');

height, width = imagePhoto.shape[:2];

for h in range(height) :
    for w in range(width):
        R = imagePhoto[h,w, 0]
        G = imagePhoto[h,w, 1]
        B = imagePhoto[h,w,2]
        
        # use Formula 
        imagePhoto[h,w] = 0.299*R + 0.587*G + 0.114*B
cv.imshow('Gray Scale Image', imagePhoto)
cv.waitKey(0)