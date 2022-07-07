import pygame
from pygame import event



def inserirBarco():
    pass


def cliqueEsquerdo():

    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pos()
    if clique[0]:
        return True, mouse