import cv2
readimg = cv2.imread('fruit2.jpg')
maskSobelX = [[-1,0,1], [-2,0,2], [-1,0,1]]
maskSobelY = [[1,2,1], [0,0,0], [-1,-2,-1]]

mOutImg = readimg.copy()
#extract height and width
h, w, ch = readimg.shape
print(w,h,ch)
#initailize 0
pTmpXB = (w*h)*[0]
pTmpXG = (w*h)*[0]
pTmpXR = (w*h)*[0]
pTmpYB = (w*h)*[0]
pTmpYG = (w*h)*[0]
pTmpYR = (w*h)*[0]
#initailize image to black or 0
mOutImg = mOutImg * 0
#apply mask to original image
for i in range(1,h-1):
    for j in range(1,w-1):
        newValueBx = 0
        newValueGx = 0
        newValueRx = 0
        newValueBy = 0
        newValueGy = 0
        newValueRy = 0
        # I1(i+k-1,j+l-1)*k(k,l) --> mc=k; mr=l
        for mr in range(3):
            for mc in range(3):
                # I1(i+k-1,j+l-1)
                r,g,b = readimg[i+mc-1,j+mr-1] 
                # k(k,l) = maskSobelX[mr][mc]
                newValueBx += maskSobelX[mr][mc]*b
                newValueGx += maskSobelX[mr][mc]*g
                newValueRx += maskSobelX[mr][mc]*r
                newValueBy += maskSobelY[mr][mc]*b
                newValueGy += maskSobelY[mr][mc]*g
                newValueRy += maskSobelY[mr][mc]*r
        pTmpXB[i*w+j] = newValueBx
        pTmpXG[i*w+j] = newValueGx
        pTmpXR[i*w+j] = newValueRx
        pTmpYB[i*w+j] = newValueBy
        pTmpYG[i*w+j] = newValueGy
        pTmpYR[i*w+j] = newValueRy
#convert to positive
for i in range(1,h-1):
    for j in range(1,w-1):
        constBVal1,constGVal1,constRVal1=pTmpXB[i*w+j],pTmpXG[i*w+j],pTmpXR[i*w+j]
        constBVal2,constGVal2,constRVal2=pTmpYB[i*w+j],pTmpYG[i*w+j],pTmpYR[i*w+j]
        if constBVal1<0:
            constBVal1 = -constBVal1
        if constGVal1<0:
            constGVal1 = -constGVal1
        if constRVal1<0:
            constRVal1 = -constRVal1
        if constBVal2<0:
            constBVal2 = -constBVal2
        if constGVal2<0:
            constGVal2 = -constGVal2
        if constRVal2<0:
            constRVal2 = -constRVal2
        pTmpXB[i*w+j] = constBVal1+constBVal2
        pTmpXG[i*w+j] = constGVal1+constGVal2
        pTmpXR[i*w+j] = constRVal1+constRVal2
#new max and min of picture
minB=minG=minR=100000000
maxB=maxG=maxR=-100000000
for i in range(1,h-1):
    for j in range(1,w-1):
        newValueB=pTmpXB[i*w+j]
        newValueG=pTmpXG[i*w+j]
        newValueR=pTmpXR[i*w+j]
        if(newValueB<minB):
            minB = newValueB
        if(newValueB>maxB):
            maxB = newValueB
        if(newValueG<minG):
            minG = newValueG
        if(newValueG>maxG): 
            maxG = newValueG
        if(newValueR<minR):
            minR = newValueR
        if(newValueR>maxR):
            maxR = newValueR
# normalize number --> can be range from 0 to 1 (original from 0 to 255)
constBVal1 = (float(255.0/(maxB-minB)))
constBVal2 = (float(-255.0*minB/(maxB-minB)))
constGVal1 = (float(255.0/(maxG-minG)))
constGVal2 = (float(-255.0*minG/(maxG-minG)))
constRVal1 = (float(255.0/(maxR-minR)))
constRVal2 = (float(-255.0 * minR/(maxR-minR)))
# apply new RGB
#for i in range(1,h-1):
  #for j in range(1,w-1):
        # Write your code here

pTmpXB = []
pTmpXG = []
pTmpXR = []
pTmpYB = []
pTmpYG = []
pTmpYR = []
cv2.imshow("Sobel Edge Detection",mOutImg)
cv2.imshow("Origin",readimg)
cv2.waitKey()
