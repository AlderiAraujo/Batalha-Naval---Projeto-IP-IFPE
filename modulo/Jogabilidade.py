import pygame


class Jogabilidade:

    def inserirBarco(self):
        pass


    def cliqueEsquerdo(self):

        mouse = pygame.mouse.get_pos()
        clique = pygame.mouse.get_pos()
        if clique[0]:
            return True, mouse

    def tiro(self):
        pass
