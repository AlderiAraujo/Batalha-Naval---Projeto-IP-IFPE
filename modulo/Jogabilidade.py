import pygame
from modulo.embarcacoes import Embarcacao


class Jogabilidade:

    def avaliaCliqueTabuleiro(self, matrizTabuleiro, pos_x, pos_y):

        mouse = pygame.mouse.get_pos()
        self.pos_clicada = ()
        self.pos_tela = ()
        y = pos_y
        for l in range(0, 8):
            x = pos_x
            for c in range(0, 8):
                if mouse[0] and matrizTabuleiro[l][c].get_rect(topleft=(x, y)).collidepoint(mouse):
                    print("clique funcionando")
                    self.pos_clicada = (l, c)
                    self.pos_tela = (x, y)
                    return self.pos_clicada, self.pos_tela
                x += 50
            y += 50

    def inserirBarco(self, nome):

        self.nome = nome
        if self.nome == 'submarino':
            self.tipo = Embarcacao(self.nome)
            return self.tipo


    def tiro(self):
        pass
