import cv2 as cv;

img = cv.imread("./images/facetree.jpg");

height, width = img.shape[:2];

mirrImg1 =  mirrImg2 =  mirrImg3 = img.copy()

def mirrImg1(img):
    for h in range(height):
        for w in range(width):
            mirrImg1[h,w] = img[h,w-1]
        return mirrImg1

            
    