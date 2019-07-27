#Import de bibliotecas
import cv2
import numpy as np
#Filtro gaussianBlur pronto!
image = cv2.imread('lena_std.tiff')
GParameter = input('Insira o parametro para o filtro Gaussian Blur')
#Tive que usar o comando 'int()' para converter a entreda do parametro, pois após alguns testes
#o script começou a dar erro, apontando que a variavel estava recebendo uma String,.
GParameter= int(GParameter)
gaussianBlur = cv2.GaussianBlur(image,(GParameter,GParameter),0)
cv2.imshow("Filtro GaussianBlur",gaussianBlur)
cv2.waitKey(0)
