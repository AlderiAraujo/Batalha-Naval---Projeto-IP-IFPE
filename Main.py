import pygame
from Modulo.Tabuleiro import FundoTabuleiro, TabuleiroPlayer1, TabuleiroPlayer2
from Modulo.Jogabilidade import InserirBarco

tela = pygame.display.set_mode((1060,500))
pygame.display.set_caption("Batalha Naval")
RED = (255, 0, 0)

continuar = True
while continuar:
    for event in pygame.event.get():
        pygame.draw.rect(tela, RED, [525, 0, 10, 500])  # linha divisória dos tabuleiros
        if event.type == pygame.QUIT:   #condição para saída do loop de eventos, apertando o botão "X" da janela
            continuar = False
    #funções de tabuleiro
        FundoTabuleiro()
        TabuleiroPlayer1()
        TabuleiroPlayer2()
    #funções de jogabilidade



    pygame.display.update() #comando para atualização de frame