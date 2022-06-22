import pygame
#variáveis usadas para a criação do tabuleiro
tabuleiro = []
linha = 8
coluna = 8
AZUL = (0, 0, 255)
#img_oceano = pygame.image.load('./Batalha-Naval---Projeto-IP-IFPE/Modulo/oceano.jpg')

#loop para criação da matriz
for l in range(0, linha):
    listaLinha = []
    for c in range(0, coluna):
        listaLinha.append(0)
    tabuleiro.append(listaLinha)

#impressão da matriz do tabuleiro
print(f'\tA \tB \tC \tD \tE \tF \tG \tH')
IDLinhaInicial = 1
for pos,item in enumerate(tabuleiro):
    IDLinha = IDLinhaInicial + pos
    print(IDLinha, item)

