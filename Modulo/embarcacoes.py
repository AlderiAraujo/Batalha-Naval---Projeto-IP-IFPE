import pygame

altura = largura = 48
class Embarcacao:

    def __init__(self, nome):

        self.nome = nome
        self.img = None

        if self.nome == "submarino":
            self.imgSubmarino = pygame.image.load("./modulo/Repositorio-Imagens/submarino.png")
            self.imgSubmarinoFormat = pygame.transform.scale(self.imgSubmarino, (largura, altura))
            self.quantidade = 5
            self.pontuacao = 1
            self.img = self.imgSubmarinoFormat

        elif self.nome == "cruzador":
            self.imgCruzador = pygame.image.load("./modulo/Repositorio-Imagens/cruzador.png")
            self.imgCruzadorFormat = pygame.transform.scale(self.imgCruzador, (largura, altura))
            self.quantidade = 3
            self.pontuacao = 2
            self.img = self.imgCruzadorFormat


        elif self.nome == "portaAvioes":
            self.imgPortaAvioes = pygame.image.load("./modulo/Repositorio-Imagens/portaAvioes.png")
            self.imgPortaAvioesFormat = pygame.transform.scale(self.imgPortaAvioes, (largura, altura))
            self.quantidade = 1
            self.pontuacao = 4
            self.img = self.imgPortaAvioesFormat









