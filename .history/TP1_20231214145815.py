import cv2 as cv;


imageFile = cv.imread('./images/Test1.jpg');


height, width = imageFile.shape[:2]

new_grayScale = imageFile.copy()


print(imageFile.shape)
for h in range(height) :
    for w in range(width) :
        B = imageFile[h,w, 0]
        G = imageFile[h,w, 1]
        R = imageFile[h,w, 2]
        # Use RGB's Formula RGB = 0.299*R + 0.587*G + 0.114*B
        intensity = imageFile[h,w] = 0.114*B + 0.587*G + 0.299*R
        
        new_grayScale[h,w] = [intensity, intensity, intensity]
    
cv.imshow('OrignalScale', imageFile)
cv.imshow('GrayScale', new_grayScale)
cv.waitKey(0)
cv.destroyAllWindows()        


