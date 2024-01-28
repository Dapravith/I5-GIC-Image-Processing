import cv2 as cv;


imageFile = cv.imread('./images/Test1.jpg');

height, width = imageFile.shape[:2]


for h in range(height) :
    for w in range(width) :
        R = imageFile[h,w,0]
        G = imageFile[h,w,1]
        B = imageFile[h,w,2]
        
        # Use RGB's Formula RGB = 0.299*R + 0.587*G + 0.114*B
        
        imageFile[h,w] = 0.299*R + 0.587*G + 0.114*B
cv.imshow('GrayScale', imageFile)
cv.waitKey(0)        


