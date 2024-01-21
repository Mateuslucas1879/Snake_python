import pygame
import random

pygame.init()

# Cores Utilizadas
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Configurações de Tela e Jogo
screen_width = 600
screen_height = 400
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da Cobra")

# Inicialização de Fontes e Relógio
font = pygame.font.SysFont(None, 35)
game_over_font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

# Configuração inicial da cobra
snake_size = 20
init_velocity = 20
snake_x = screen_width // 2
snake_y = screen_height // 2
velocity_x = 0
velocity_y = 0
score = 0
fps = 10

# Posição inicial da comida
food_x, food_y = random.randrange(0, screen_width - snake_size, snake_size), random.randrange(0, screen_height - snake_size, snake_size)

def food_generation():
    return random.randrange(0, screen_width - snake_size, snake_size), random.randrange(0, screen_height - snake_size, snake_size)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(tamanho, snake_list):
    for snake_head in snake_list:
        pygame.draw.rect(game_window, white, [snake_head[0], snake_head[1], tamanho, tamanho])

# Loop principal do jogo
exit_game = False
snake_list = []
length_of_snake = 1

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
            elif event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0
            elif event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    # Atualização da posição da cobra
    snake_x += velocity_x
    snake_y += velocity_y

    # Verificação de colisões
    if (
        snake_x < 0 or snake_x + snake_size > screen_width or
        snake_y < 0 or snake_y + snake_size > screen_height
    ):
        exit_game = True

    # Desenho da tela
    game_window.fill(black)
    pygame.draw.rect(game_window, green, [food_x, food_y, snake_size, snake_size])

    # Desenho da cobra
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)

    if len(snake_list) > length_of_snake:
        del snake_list[0]

    # Verificação de colisão com o corpo da cobra
    if snake_head in snake_list[:-1]:
        exit_game = True

    plot_snake(snake_size, snake_list)

    # Verificação de colisão com a comida
    if (
        snake_x < food_x + snake_size and snake_x + snake_size > food_x and
        snake_y < food_y + snake_size and snake_y + snake_size > food_y
    ):
        food_x, food_y = food_generation()
        length_of_snake += 1
        score += 1

    # Exibição da pontuação
    text_screen(f'Pontuação: {score}', red, 5, 5)

    # Atualização da tela
    pygame.display.update()
    clock.tick(fps)

# Exibição da mensagem "Game Over"
game_over_text = game_over_font.render("Game Over", True, white)
game_window.blit(game_over_text, (screen_width // 4, screen_height // 3))
pygame.display.update()

# Aguardar alguns segundos antes de fechar a janela
pygame.time.wait(2000)

pygame.quit()
quit()
