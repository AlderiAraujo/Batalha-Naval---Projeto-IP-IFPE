import pygame
#variáveis usadas para a criação do tabuleiro
tabuleiro1 = []
tabuleiro2 = []
indice_alfa = []
linha = 9
coluna = 9

tela = pygame.display.set_mode((1130,530))
img_oceano = pygame.image.load("C:/Users/Alderi/Documents/GitHub/Batalha-Naval---Projeto-IP-IFPE/Modulo/oceano.jpg")
img_oceanoTabuleiro = pygame.transform.scale(img_oceano, (48,48))
img = pygame.image.load("C:/Users/Alderi/Documents/GitHub/Batalha-Naval---Projeto-IP-IFPE/Modulo/branco.jpg")
img_Tabuleiro = pygame.transform.scale(img, (48,48))

#loop para criação da matriz
for i in range(9):
    indice_alfa.append(img_Tabuleiro)

for l in range(0, linha):
    listaLinha = []
    for c in range(0, coluna):
        if tabuleiro1[0]:
            tabuleiro1[0] = indice_alfa
    tabuleiro1.append(listaLinha)

for l in range(0, linha):
    listaLinha = []
    for c in range(0, coluna):
        listaLinha.append(img_oceanoTabuleiro)
    tabuleiro2.append(listaLinha)

#impressão da matriz do tabuleiro
print(f'\tA \tB \tC \tD \tE \tF \tG \tH')
IDLinhaInicial = 1
for pos,item in enumerate(tabuleiro1):
    IDLinha = IDLinhaInicial + pos
    print(IDLinha, item)

sair = True
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #condição para saída, apertando o botão "X" da janela
            sair = False

    pos_y = 50
    for l in range(0, linha):
        pos_x = 50
        for c in range(0, coluna):
            tela.blit(tabuleiro1[l][c], (pos_x, pos_y))
            pos_x+= 50
        pos_y+=50

    pos_y = 50
    for l in range(0, linha):
        pos_x = 610
        for c in range(0, coluna):
            tela.blit(tabuleiro2[l][c], (pos_x, pos_y))
            pos_x += 50
        pos_y += 50

    pygame.display.update() #comando para atualização de frame