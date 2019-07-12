import cv2
import numpy as np
##vamos ler nossa querida lena, e vamos selecionar um pixel de sua imagem.
img = cv2.imread('lena_std.tif')
##mostramos a lena, e então usamos uma váriavel para receber as cordenadas de linha e coluna
##e então podemos imprimir o valor RGB desse pixel.
cv2. imshow('lena_std.tif',img)
pix = img[500,510]
print (pix)


##No codigo abaixo, é modificado o pixel 1-1 da matriz da imagem para o valor RGB 43, 239, 102, verde
## para podermos encontra-lo facilmente.
## e depois imprime a imagem, 
img[0,0]= [43, 239, 102]
print (img[1,1])
cv2. imshow('lena_std.tif',img)
