import cv2 as cv

img = cv.imread('./images/facetree.jpg')


height, width = img.shape[:2]

mirImg1 = mirImg2 = img.copy()

def  miro_img1(img):
        for h in range(height):
            for w in range(width):
                mirImg1[h,w]=img[1-h,w]
        return mirImg1
def miro_img2(img):
    for h in range(height):
        for w in range(width):
            mirImg2[h,w]=img[h,1-w]
    return mirImg2




cv.imshow('Test1',img)

cv.imshow('Test2', miro_img1(img))

cv.imshow('Test3', miro_img2(img))

cv.waitKey(0)
cv.destroyAllWindows()