import sys
import cv2

print("Python version: \n" + sys.version)
print("cv2 version: " + cv2.__version__)

#img1 and img2 must be in same size
img1 = cv2.imread('lena_std.tif', 1)
hsv1 = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv1)


##Mostrando a imagem original
cv2.imshow('img1',img1)
##Mostrando cada imagem seeparadamente
cv2.imshow('hsv1',hsv1)
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)

cv2.imwrite("H.png", h)
cv2.imwrite("S.png", s)
cv2.imwrite("V.png", v)
cv2.imwrite("HSV1.png", hsv1)

cv2.waitKey(0)
cv2.destroyAllWindow()
