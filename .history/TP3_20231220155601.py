import cv2 as cv

img = cv.imread('./images/facetree.jpg')
width, height = img.shape[:2]

mirrorImg1 = mirrorImg2 = mirrorImg3 = img.copy()

def mirror_ImgF1(img):
    mirrored_image = img.copy()
    for h in range(height):
        for w in range(width):
            mirrored_image[h][w] = img[height - 1 - h][w]
    return mirrored_image

def mirror_ImgF2(img):
    mirrored_image = img.copy()
    for h in range(height):
        for w in range(width):
            mirrored_image[h][w] = img[h][width - 1 - w]
    return mirrored_image

def mirror_ImgF3(img):
    mirrored_image = img.copy()
    for h in range(height):
        for w in range(width):
            mirrored_image[h][w] = img[height - 1 - h][width - 1 - w]
    return mirrored_image

cv.imshow('Original', img)
cv.imshow('Mirror1', mirror_ImgF1(img))
cv.imshow('Mirror2', mirror_ImgF2(img))
cv.imshow('Mirror3', mirror_ImgF3(img))

cv.waitKey(0)
cv.destroyAllWindows()
