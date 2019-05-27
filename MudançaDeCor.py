import cv2
#no canal  HSV  hue : 0  - 180 , Saturation : 0 -255 , value : 255

img  =  cv2.imread('t.jpg')

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
TEMP4 = img_HSV
cv2.imshow('imagem HSV',img_HSV)

cv2.imshow('HUE ', img_HSV[ : , : , 0])
TEMP1 = img_HSV[ : , : , 0]
cv2.imshow('SATURATION', img_HSV[ : , : , 1])
TEMP2 = img_HSV[ : , : , 1]
cv2.imshow('VALUE CHANNEL', img_HSV [ : , : , 2])
TEMP3 = img_HSV[ : , : , 2]

cv2.imwrite("HUE.png", TEMP1)
cv2.imwrite("SATURATION.png", TEMP2)
cv2.imwrite("VALUE CHANNEL.png", TEMP3)
cv2.imwrite("HSV.png", TEMP4)


cv2.waitKey(0)
cv2.destroyAllWindows()
