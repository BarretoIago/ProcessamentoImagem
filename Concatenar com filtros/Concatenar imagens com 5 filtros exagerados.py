import cv2
import numpy as np
    #Aqui carregamos uma imagem dentro de uma váriavel, importante notar que o arquivo 't.jpg'  deve estar no mesmo diretorio
    # que o arquivo de execução
img = cv2.imread('lena_std.tiff')
    #abaixo criamos uma janela onde a imagem carregada será mostrada, e passamos como parametros o nome que daremos
    #a janela e a variavel que contem a imagem. Por motivos de organização, comentar esta linha para não abrir duas
    #janelas.
cv2.imshow('Imagem Original',img)

Rimg= cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow('Imagem Redimensionada',Rimg)
 #################################
    #após carregarmos a imagem, podemos trata-la como alguns filtros, abaixo aplicamos alguns, importante
    #notar que cada filtro é carregado em uma imagem clonada.

kernel = np.ones((6,6),np.float32)/25
filter2D = cv2.filter2D(Rimg,-1,kernel)
blur = cv2.blur(Rimg,(5,5))
    #importante mencionar que no filtro gaussianBlur, passamos apenas numeros iguais e  impares
gaussianBlur = cv2.GaussianBlur(Rimg,(61,61),0)
median = cv2.medianBlur(Rimg,9)
bilateralFilter = cv2.bilateralFilter(Rimg,9,75,75)
    #abaixo, para melhor analisarmos os resultados dos filtros, coloquei uma identificação em cada clone com seu
    #respectivo filtro
font = cv2.FONT_HERSHEY_DUPLEX 

cv2.putText(Rimg,'Sem Filtros',(5,50), font, 0.5, (255,0,0), 1, cv2.LINE_AA)
 
cv2.putText(filter2D,'Filter 2D',(45,50), font, 0.5, (255,0,0), 1, cv2.LINE_AA)

cv2.putText(blur,'Blur',(80,50), font, 0.5, (255,0,0), 1, cv2.LINE_AA)

cv2.putText(gaussianBlur,'Gaussian Blur',(10,50), font, 0.5, (255,0,0), 1, cv2.LINE_AA)

cv2.putText(median,'Median',(60,50), font, 0.5, (255,0,0), 1, cv2.LINE_AA)

cv2.putText(bilateralFilter,'Bilateral Filter',(10,50), font, 0.5, (255,0,0), 1, cv2.LINE_AA)

#abaixo concateno a imagem para abrirmos apenas uma unica janela onde vemos todas as imagens lado-a-lado
tempImage1 = np.concatenate((Rimg, median, gaussianBlur), axis=1)
tempImage2 = np.concatenate((bilateralFilter, blur, filter2D), axis=1)
FinalImage = np.concatenate((tempImage1, tempImage2), axis=0)
    #################################
    # então salvo uma copia da imagem no mesmo repositorio da original
cv2.imwrite("image.png", FinalImage)
    # aqui abrimos a imagem final concatenada em uma janela
cv2.imshow("Final Image", FinalImage)
    #################################
cv2.waitKey(0)
    #fecha todas as janelas ao fechar a imagem, caso existam mais imagens abertas
cv2.destroyAllWindows()
    ###########################################

