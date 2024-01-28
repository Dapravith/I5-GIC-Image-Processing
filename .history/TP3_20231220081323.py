import cv2 as cv

img = cv.imread('./images/facetree.jpg')
width, height = img.shape[:2]

mirrorImg1 = mirrorImg2 = mirrorImg3 = img.copy()

def mirror_ImgF1(img):
    for h in range (height):
        for w in range (width):
            mirror_ImgF1[h,w] = img[1-h, w]
            return mirror_ImgF1
        
def mirror_ImgF2(img):
    for h in range (height):
        for w in range (width):
            mirror_ImgF2[h,w] = img[h, 1-w]
            return mirror_ImgF2

def mirror_ImgF3(img):
    for h in range (height):
        for w in range (width):
            mirror_ImgF3[h,w] = img[1-h, 1-w]
            return mirror_ImgF3


cv.imshow('Test2', mirror_ImgF1(img))

cv.imshow('Test3', mirror_ImgF2(img))

cv.imshow('Test4', mirror_ImgF3(img))

cv.waitKey(0)
cv.destroyAllWindows()
