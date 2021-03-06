import cv2 as cv
import numpy as np
img = cv.imread("images/LeBron_James_crop.jpg")
print(img.shape)


cv.imshow("Lebron James",img)

#translation +x --> right +y --> down
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img,100,100);
cv.imshow("Translated right and down by 100 pixels",translated)


#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,90)
cv.imshow("Rotated by 90 degree", rotated)

#flipping
flip = cv.flip(img,1)
cv.imshow('Flip Horizontally ',flip)
cv.waitKey(0)
        