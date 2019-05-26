import cv2
import numpy as np
img = cv2.imread('t.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imshow('nomeDaTela',img)
