import cv2
import numpy as np
##vamos ler nossa querida lena, e vamos selecionar um pixel de sua imagem.
img = cv2.imread('lena_std.tif')
numR= input("Digite um número para o tom RED:")
numG= input("Digite um número para o tom GREEN:")
numB= input("Digite um número para o tom BLUE:")

py=input("Digite  a cordenada Y do pixel:")
px=input("Digite  a cordenada X do pixel:")
##vamos tentar receber os dados do usuário

print("Cor original do pixel")
print (img['py,px'])
img[py,px]= [numR, numG, numB]
cv2. imshow('lena_std.tif',img)

##mostramos a lena, e então usamos uma váriavel para receber as cordenadas de linha e coluna
##e então podemos imprimir o valor RGB desse pixel.

pix = img[py,px]
print("Nova cor do pixel")
print (pix)
