import pygame

altura = largura = 48
class Embarcacao:

    def __init__(self, nome, imagem, quantidade, pontuacao):

        self.nome = nome
        self.imagem = imagem
        self.quantidade = quantidade
        self.pontuacao = pontuacao

        if self.nome == "submarino":
            self.ImgSubmarino = pygame.image.load("./Repositorio-Imagens/submarino.png")
            self.ImgSubmarinoFormat = pygame.transform.scale(self.ImgSubmarino, (largura, altura))
            self.quantidade = 5
            self.pontuacao = 1


        elif self.nome == "cruzador":
            self.ImgCruzador = pygame.image.load("./Repositorio-Imagens/cruzador.png")
            self.ImgCruzadorFormat = pygame.transform.scale(self.ImgCruzador, (largura, altura))
            self.quantidade = 3
            self.pontuacao = 2


        elif self.nome == "portaAvioes":
            self.ImgPortaAvioes = pygame.image.load("./Repositorio-Imagens/portaAvioes.png")
            self.ImgPortaAvioesFormat = pygame.transform.scale(self.ImgPortaAvioes, (largura, altura))
            self.quantidade = 1
            self.pontuacao = 4








