import cv2
import numpy as np
    #Aqui carregamos uma imagem dentro de uma váriavel, importante notar que o arquivo 't.jpg'  deve estar no mesmo diretorio
    # que o arquivo de execução
img = cv2.imread('t.jpg')
    #abaixo criamos uma janela onde a imagem carregada será mostrada, e passamos como parametros o nome que daremos
    #a janela e a variavel que contem a imagem. Por motivos de organização, comentar esta linha para não abrir duas
    #janelas.
cv2.imshow('nomeDaTela',img)
 #################################
    #após carregarmos a imagem, podemos trata-la como alguns filtros, abaixo aplicamos alguns, importante
    #notar que cada filtro é carregado em uma imagem clonada.

kernel = np.ones((6,6),np.float32)/25
filter2D = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gaussianBlur = cv2.GaussianBlur(img,(555,555),0)
median = cv2.medianBlur(img,9)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)
    #abaixo, para melhor analisarmos os resultados dos filtros, coloquei uma identificação em cada clone com seu
    #respectivo filtro
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img,'Original Image',(5,50), font, 3, (255,0,0), 3, cv2.LINE_AA)
cv2.putText(filter2D,'Filter 2D',(45,50), font, 3, (255,0,0), 3, cv2.LINE_AA)
cv2.putText(blur,'Blur',(80,50), font, 3, (255,0,0), 3, cv2.LINE_AA)
cv2.putText(gaussianBlur,'Gaussian Blur',(10,50), font, 3, (255,0,0), 3, cv2.LINE_AA)
cv2.putText(median,'Median',(60,50), font, 3, (255,0,0), 3, cv2.LINE_AA)
cv2.putText(bilateralFilter,'Bilateral Filter',(10,50), font, 3, (255,0,0), 3, cv2.LINE_AA)
#abaixo concateno a imagem para abrirmos apenas uma unica janela onde vemos todas as imagens lado-a-lado
tempImage1 = np.concatenate((img, median, gaussianBlur), axis=1)
tempImage2 = np.concatenate((bilateralFilter, blur, filter2D), axis=1)
finalImage = np.concatenate((tempImage1, tempImage2), axis=0)
    #################################
    # então salvo uma copia da imagem no mesmo repositorio da original
cv2.imwrite("image.png", finalImage)
    # aqui abrimos a imagem final concatenada em uma janela
cv2.imshow("Final Image", finalImage)
    #################################
cv2.waitKey(0)
    #fecha todas as janelas ao fechar a imagem, caso existam mais imagens abertas
cv2.destroyAllWindows()
    ###########################################

