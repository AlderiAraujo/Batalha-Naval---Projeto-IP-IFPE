import pygame
from pygame import event



def inserirBarco():

    X = pygame.mouse.get_pos()[0]
    Y = pygame.mouse.get_pos()[1]


def verificaClique():

    posicao_mouse = pygame.mouse.get_pos()
    posX_mouse, posY_mouse = posicao_mouse

    print(posicao_mouse)
    print(posX_mouse, posY_mouse)
    return posicao_mouse

