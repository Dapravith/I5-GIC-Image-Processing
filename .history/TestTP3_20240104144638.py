import cv2 as cv;

img = cv.imread("./images/facetree.jpg");

height, width = img.shape[:2];

mirrImg1 =  mirrImg2 =  mirrImg3 = img.copy()

def mirrImg1(img):
    for h in range(height):
        for w in range(width):
            mirrImg1[h,w] = img[1-h, w]
        return mirrImg1

def mirrImg2(img): 
    for h in range(height):
        for w in range(width):
            mirrImg2[h,w] = img[h,1-w]
        return mirrImg2


cv.imshow('Image 1', img);
cv.imshow('Image 2', mirrImg1(img));
cv.imshow('Image 3', mirrImg2(img));
    