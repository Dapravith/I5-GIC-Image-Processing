import cv2 as cv;
import numpy as num;

img = cv.imread('./img/cart.png');

height, width = img.shape[:2]


for h in range(height) :
    for w in range(width) :
        R = img[h,w,0]
        G = img[h,w,1]
        B = img[h,w,2]
        
        #img[h,w] = R + G + B
        
        img[h,w] = 0.299*R + 0.587*G + 0.114*B
cv.imshow('GrayScale', img)
cv.waitKey(0)        

