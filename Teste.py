#Arquivo cópia do Main para efeito de teste, deve ser apagado no fim do projeto
import pygame
from Modulo.Tabuleiro import *
from Modulo.Jogabilidade import *


tela = pygame.display.set_mode((1060,500))
pygame.display.set_caption("Batalha Naval")
RED = (255, 0, 0)
WHITE = (255, 255, 255)


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

        rect = pygame.draw.rect(tela, WHITE, (450, 450, 48, 48))
        tela.blit(ImgOceanoTabuleiro, (450, 450))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(pygame.mouse.get_pos()):
                print("clicou dentro")
            else:
                print("clicou fora")

    #funções de jogabilidade




    pygame.display.update() #comando para atualização de frame