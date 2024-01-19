### Definição:
Pygame é uma biblioteca em Python que fornece funcionalidades para o desenvolvimento de jogos e aplicações multimídia. 
Ele é construído sobre a biblioteca SDL (Simple DirectMedia Layer) e oferece uma interface simplificada para gráficos, áudio e entrada de usuário

### Funcionalidades Principais:

Gráficos: O Pygame permite criar janelas, desenhar formas geométricas, imagens, e manipular pixels na tela.
Som e Música: Oferece suporte para reprodução de efeitos sonoros e música de fundo.
Entrada do Usuário: Captura eventos de teclado, mouse e outros dispositivos de entrada.
Colisões: Facilita a detecção de colisões entre objetos na tela.
Temporização: Controla a taxa de quadros por segundo (FPS) e permite criar animações suaves.

### Elementos Principais:

Surface: É a área retangular da tela onde você desenha. Pode representar a tela inteira ou uma parte dela.
Sprites: Objetos gráficos que podem ser movidos e interagir no jogo.
Eventos: Pygame utiliza um sistema de eventos para capturar ações do usuário, como pressionar teclas ou mover o mouse.
Clock: Ajuda a controlar a taxa de quadros e o tempo no jogo.

### Exemplo Simples de Código Pygame:

import pygame
pygame.init()

# Configurações iniciais
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica do jogo e desenho na tela aqui

    pygame.display.flip()

pygame.quit()

