import pygame
#variáveis usadas para a criação do tabuleiro
linha = 8
coluna = 8
RED = (255, 0, 0)

tabuleiro = []
IndiceAlfa = []
IndiceNum = []

tela = pygame.display.set_mode((1060,480))  #dimensões do tabuleiro na janela

#load e redimensionamento de imagem de fundo e loop para criação de matriz para o tabuleiro
ImgOceano = pygame.image.load("./Repositorio-Imagens/oceano.jpg")
ImgOceanoTabuleiro = pygame.transform.scale(ImgOceano, (48,48))
for l in range(0, linha):
    listaLinha = []
    for c in range(0, coluna):
        listaLinha.append(ImgOceanoTabuleiro)
    tabuleiro.append(listaLinha)

#loop para load, redimensionamento e adição de imagens dos índices alfabeticos(colunas) em lista
base = 65
for cont in range (0, linha):
    atual = base + cont
    Img = pygame.image.load(f"./Repositorio-Imagens/Img{atual}.jpg")
    TabuleiroImg = pygame.transform.scale(Img, (48, 48))
    IndiceAlfa.append(TabuleiroImg)
#loop para load, redimensionamento e adição de imagens dos índices numericos(linhas) em lista
base = 1
for cont in range (0, linha):
    atual = base + cont
    Img = pygame.image.load(f"./Repositorio-Imagens/Img{atual}.jpg")
    TabuleiroImg = pygame.transform.scale(Img, (48, 48))
    IndiceNum.append(TabuleiroImg)

#loop para geração de eventos
continuar = True
while continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #condição para saída do loop de eventos, apertando o botão "X" da janela
            continuar = False
    pygame.draw.rect(tela,RED, [525,0,10,480])  #linha divisória dos tabuleiros

#loops para posicionamento das imagens dos tabuleiros na janela
#loop para posicionamento dos índices alfabeticos(colunas) do tabuleiro 1
    pos_y = 0
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(IndiceAlfa[c], (pos_x, pos_y))
            pos_x += 50
#loop para posicionamento dos índices numéricos(linhas) do tabuleiro 1
    pos_y = 50
    for l in range(0, linha):
        pos_x = 0
        for c in range(0, coluna):
            tela.blit(IndiceNum[l], (pos_x, pos_y))
        pos_y += 50
#loop para posicionamento da matriz de fundo do tabuleiro 1
    pos_y = 50
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(tabuleiro[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50

#loop para posicionamento dos índices alfabeticos(colunas) do tabuleiro 2
    pos_y = 0
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(IndiceAlfa[c], (pos_x, pos_y))
            pos_x += 50
#loop para posicionamento dos índices numéricos(linhas) do tabuleiro 2
    pos_y = 50
    for l in range(0, linha):
        pos_x = 1010
        for c in range(0, coluna):
            tela.blit(IndiceNum[l], (pos_x, pos_y))
        pos_y += 50
#loop para posicionamento da matriz de fundo do tabuleiro 2
    pos_y = 50
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(tabuleiro[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50

    pygame.display.update() #comando para atualização de frame