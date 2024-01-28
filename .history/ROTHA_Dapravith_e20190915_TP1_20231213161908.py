import cv2 as cv;
import numpy as num;

img1 = cv.imread('./img/cart.png');

height, width = img1.shape[:2]


for h in range(height) :
    for w in range(width) :
        R = img1[h,w,0]
        G = img1[h,w,1]
        B = img1[h,w,2]
        
        #img1[h,w] = R + G + B
        
        img1[h,w] = 0.299*R + 0.587*G + 0.114*B
cv.imshow('GrayScale', img1)
cv.waitKey(0)        

