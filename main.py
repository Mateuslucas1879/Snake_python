import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600
gamewind = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Jogo da Cobra")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewind.blit(screen_text, [x, y])

def plot_snake(gamewind, color, snk_list, snake_size):
    for i, (x, y) in enumerate(snk_list):
        pygame.draw.rect(gamewind, color if i % 2 == 0 else white, [x, y, snake_size, snake_size])

# Configuração inicial da cobra
snake_list = []
length_of_snake = 1
snake_size = 20
init_velocity = 20
snake_x = screen_width / 2
snake_y = screen_height / 2
velocity_x = 0
velocity_y = 0
food_x = random.randint(20, screen_width - 20)
food_y = random.randint(60, screen_height - 20)
score = 0
fps = 10

exit_game = False
game_over = False

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

    snake_x += velocity_x
    snake_y += velocity_y

    if snake_x < 0 or snake_x + snake_size > screen_width or snake_y < 0 or snake_y + snake_size > screen_height:
        game_over = True

    gamewind.fill(white)
    pygame.draw.rect(gamewind, red, [food_x, food_y, snake_size, snake_size])

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    plot_snake(gamewind, black, snake_list, snake_size)

    # Verificar colisão com a comida
    if snake_x < food_x + snake_size and snake_x + snake_size > food_x and snake_y < food_y + snake_size and snake_y + snake_size > food_y:
        food_x = random.randint(20, screen_width - 20)
        food_y = random.randint(60, screen_height - 20)
        length_of_snake += 1
        score += 10

    text_screen(f'Pontuação: {score}', black, 5, 5)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
