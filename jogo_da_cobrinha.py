import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Dimenções
altura = 480
largura = 640

x_cobra = largura / 2
y_cobra = altura/2

x_maça = randint(40, 620)
y_maça = randint(50, 460)

velocidade = 10
x_controle = velocidade
y_controle = 0

som_de_pontuação = pygame.mixer.Sound('Efeito sonoro da moeda do Mario(MP3_128K).mp3')

#Criação da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake game')

fonte = pygame.font.SysFont('arial', 20, True,False)
pontos = 0
lista_corpo = []
comprimento_da_cobra = 5
game_over = False

#Controle de FPS
FPS = pygame.time.Clock()

def aumento_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20,20))

def reiniciar():
    global pontos, comprimento_da_cobra, x_cobra, y_cobra,lista_corpo, lista_cabeça, x_maça, y_maça, game_over
    pontos = 0
    comprimento_da_cobra = 5
    x_cobra = largura / 2
    y_cobra = altura / 2
    x_maça = randint(40, 620)
    y_maça = randint(50, 460)
    game_over = False
    lista_cabeça = []
    lista_corpo = []

#Loop
while True:
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    FPS.tick(20)
    tela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra += x_controle
    y_cobra += y_controle


    cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra,y_cobra, 20,20))
    maça = pygame.draw.rect(tela,(255,0,0), (x_maça,y_maça, 20,20))

    if cobra.colliderect(maça):
        x_maça = randint(20, 620)
        y_maça = randint(20, 460)
        pontos += 1
        comprimento_da_cobra += 1
        som_de_pontuação.play()

    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)

    lista_corpo.append(lista_cabeça)

    #game over
    if lista_corpo.count(lista_cabeça) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over!, Precione a tecla "R" para recomeçar'
        texto_formatado = fonte2.render(mensagem, True, (255,0,0))
        ret_texto = texto_formatado.get_rect()

        game_over = True
        while game_over:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    #travesia da parede
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura

    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura


    if len(lista_corpo) > comprimento_da_cobra:
        del lista_corpo[0]

    aumento_cobra(lista_corpo)

    tela.blit(texto_formatado, (520,20))
    pygame.display.update()
