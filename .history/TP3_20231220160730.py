import cv2 as cv

img = cv.imread('./images/facetree.jpg')

height, width = img.shape[:2]

mirImg1 = mirImg2 = img.copy()

def miro_f1(img):
    for h in range(height):
        for w in range(width // 2):  # Iterate only up to half of the width
            mirImg1[h, w] = img[height - 1 - h, w]
    return mirImg1

def miro_f2(img):
    for h in range(height):
        for w in range(width // 2, width):  # Iterate from half of the width to the end
            mirImg2[h, w - width // 2] = img[h, w]
    return mirImg2

cv.imshow('Test1', img)
cv.imshow('Test2', miro_f1(img))
cv.imshow('Test3', miro_f2(img))

cv.waitKey(0)
cv.destroyAllWindows()
