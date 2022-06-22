import pygame
#variáveis usadas para a criação do tabuleiro
linha = 8
coluna = 8

tabuleiro1 = []
indice_alfa1 = []
indice_num1 = []

tabuleiro2 = []
indice_alfa2 = []
indice_num2 = []

tela = pygame.display.set_mode((1060,480))
img_oceano = pygame.image.load("./Repositorio-Imagens/oceano.jpg")
img_oceanoTabuleiro = pygame.transform.scale(img_oceano, (48,48))
imgA = pygame.image.load("./Repositorio-Imagens/A.jpg")
imgATabuleiro = pygame.transform.scale(imgA, (48,48))
imgB = pygame.image.load("./Repositorio-Imagens/B.jpg")
imgBTabuleiro = pygame.transform.scale(imgB, (48,48))
imgC = pygame.image.load("./Repositorio-Imagens/C.jpg")
imgCTabuleiro = pygame.transform.scale(imgC, (48,48))
imgD = pygame.image.load("./Repositorio-Imagens/D.jpg")
imgDTabuleiro = pygame.transform.scale(imgD, (48,48))
imgE = pygame.image.load("./Repositorio-Imagens/E.jpg")
imgETabuleiro = pygame.transform.scale(imgE, (48,48))
imgF = pygame.image.load("./Repositorio-Imagens/F.jpg")
imgFTabuleiro = pygame.transform.scale(imgF, (48,48))
imgG = pygame.image.load("./Repositorio-Imagens/G.jpg")
imgGTabuleiro = pygame.transform.scale(imgG, (48,48))
imgH = pygame.image.load("./Repositorio-Imagens/H.jpg")
imgHTabuleiro = pygame.transform.scale(imgH, (48,48))
img = pygame.image.load("./Repositorio-Imagens/H.jpg")
img_Tabuleiro = pygame.transform.scale(imgH, (48,48))





for l in range(0, linha):
    indice_alfa1.append(imgATabuleiro)

for l in range(0, linha):
    indice_num1.append(img_Tabuleiro)

#loop para criação da matriz
for l in range(0, linha):
    listaLinha = []
    for c in range(0, coluna):
        listaLinha.append(img_oceanoTabuleiro)
    tabuleiro1.append(listaLinha)

for l in range(0, linha):
    indice_alfa2.append(img_Tabuleiro)

for l in range(0, linha):
    indice_num2.append(img_Tabuleiro)

for l in range(0, linha):
    listaLinha = []
    for c in range(0, coluna):
        listaLinha.append(img_oceanoTabuleiro)
    tabuleiro2.append(listaLinha)

sair = True
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #condição para saída, apertando o botão "X" da janela
            sair = False

    pos_y = 0
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(indice_alfa1[l], (pos_x, pos_y))
            pos_x += 50

    pos_y = 50
    for l in range(0, linha):
        pos_x = 0
        for c in range(0, coluna):
            tela.blit(indice_num1[c], (pos_x, pos_y))
        pos_y += 50

    pos_y = 50
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(tabuleiro1[l][c], (pos_x, pos_y))
            pos_x+= 50
        pos_y+=50

    pos_y = 0
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(indice_alfa2[l], (pos_x, pos_y))
            pos_x += 50

    pos_y = 50
    for l in range(0, linha):
        pos_x = 1010
        for c in range(0, coluna):
            tela.blit(indice_num2[c], (pos_x, pos_y))
        pos_y += 50

    pos_y = 50
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(tabuleiro2[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50

    pygame.display.update() #comando para atualização de frame