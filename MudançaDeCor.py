import cv2
import numpy as np
#no canal  HSV  hue : 0  - 180 , Saturation : 0 -255 , value : 255

img  =  cv2.imread('t.jpg')

img_HSV = cv2.cvtcolor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('imagem HSV',img_HSV)
cv2.imshow('HUE ',img_HSV, img[ : , : , 0])
