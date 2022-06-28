import pygame
#variáveis usadas para a criação do tabuleiro
linha = 8
coluna = 8

TabuleiroFundo = []
IndiceAlfa = []
IndiceNum = []
Tabuleiro1 = []
Tabuleiro2 = []
tela = pygame.display.set_mode((1060, 500))

#load e redimensionamento de imagem de fundo e loop para criação de matriz para o fundo do tabuleiro
ImgOceano = pygame.image.load("./Modulo/Repositorio-Imagens/oceano.jpg")
ImgOceanoTabuleiro = pygame.transform.scale(ImgOceano, (48,48))
for l in range(0, linha):
    LinhaFundo = []
    for c in range(0, coluna):
        LinhaFundo.append(ImgOceanoTabuleiro)
    TabuleiroFundo.append(LinhaFundo)

#loop para load, redimensionamento e adição de imagens dos índices alfabeticos(colunas) em lista
base = 65
for cont in range(0, linha):
    atual = base + cont
    Img = pygame.image.load(f"./Modulo/Repositorio-Imagens/Img{atual}.jpg")
    TabuleiroImg = pygame.transform.scale(Img, (48, 48))
    IndiceAlfa.append(TabuleiroImg)
#loop para load, redimensionamento e adição de imagens dos índices numericos(linhas) em lista
base = 1
for cont in range(0, linha):
    atual = base + cont
    Img = pygame.image.load(f"./Modulo/Repositorio-Imagens/Img{atual}.jpg")
    TabuleiroImg = pygame.transform.scale(Img, (48, 48))
    IndiceNum.append(TabuleiroImg)

def FundoTabuleiro():   #função para adicionar o fundo do tabuleiro
    #loop para posicionamento dos índices alfabeticos(colunas) do lado 1
    pos_y = 0
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(IndiceAlfa[c], (pos_x, pos_y))
            pos_x += 50
    #loop para posicionamento dos índices numéricos(linhas) do lado 1
    pos_y = 50
    for l in range(0, linha):
        pos_x = 0
        for c in range(0, coluna):
            tela.blit(IndiceNum[l], (pos_x, pos_y))
        pos_y += 50
    #loop para posicionamento da matriz de fundo do lado 1
    pos_y = 50
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(TabuleiroFundo[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50
    #loop para posicionamento dos índices alfabeticos(colunas) do lado 2
    pos_y = 0
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(IndiceAlfa[c], (pos_x, pos_y))
            pos_x += 50
    #loop para posicionamento dos índices numéricos(linhas) do lado 2
    pos_y = 50
    for l in range(0, linha):
        pos_x = 1010
        for c in range(0, coluna):
            tela.blit(IndiceNum[l], (pos_x, pos_y))
        pos_y += 50
    #loop para posicionamento da matriz de fundo do lado 2
    pos_y = 50
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(TabuleiroFundo[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50
    return tela

#load e redimensionamento de imagem de fundo e loop para criação de matriz do tabuleiro
ImgOnda = pygame.image.load("./Modulo/Repositorio-Imagens/onda.png")
OndaTabuleiro = pygame.transform.scale(ImgOnda, (48,48))
for l in range(0, linha):
    Posicoes = []
    for c in range(0, coluna):
        Posicoes.append(OndaTabuleiro)
    Tabuleiro1.append(Posicoes)
    Tabuleiro2.append(Posicoes)

def TabuleiroPlayer1 ():    #função para adicionar o tabuleiro 1
    pos_y = 50
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(Tabuleiro1[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50
    return tela

def TabuleiroPlayer2 ():   #função para adicionar o tabuleiro 2
    pos_y = 50
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(Tabuleiro2[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50
    return tela