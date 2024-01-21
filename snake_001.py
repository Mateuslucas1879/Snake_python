import pygame
import random
import sys

# Cores Utilizadas
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Configurações de Tela e Jogo
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SNAKE_SIZE = 20
INIT_VELOCITY = 20
FPS = 10

pygame.init()
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Segunda Versão Snake Game")

# Fontes
font = pygame.font.SysFont(None, 35)
game_over_font = pygame.font.SysFont(None, 50)

def draw_snake(snake_list):
    for snake_head in snake_list:
        pygame.draw.rect(game_window, WHITE, [snake_head[0], snake_head[1], SNAKE_SIZE, SNAKE_SIZE])

def display_score(score):
    text = font.render(f'Pontuação: {score}', True, RED)
    game_window.blit(text, [5, 5])

def show_game_over():
    game_over_text = game_over_font.render("Game Over", True, WHITE)
    game_window.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
    pygame.display.update()
    pygame.time.wait(2000)

def game_loop():
    snake_list = []
    length_of_snake = 1
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2
    velocity_x = 0
    velocity_y = 0
    score = 0

    food_x, food_y = random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocity_x = -INIT_VELOCITY
                    velocity_y = 0
                elif event.key == pygame.K_RIGHT:
                    velocity_x = INIT_VELOCITY
                    velocity_y = 0
                elif event.key == pygame.K_UP:
                    velocity_y = -INIT_VELOCITY
                    velocity_x = 0
                elif event.key == pygame.K_DOWN:
                    velocity_y = INIT_VELOCITY
                    velocity_x = 0

        snake_x += velocity_x
        snake_y += velocity_y

        if (
            snake_x < 0 or snake_x + SNAKE_SIZE > SCREEN_WIDTH or
            snake_y < 0 or snake_y + SNAKE_SIZE > SCREEN_HEIGHT
        ):
            show_game_over()
            return

        game_window.fill(BLACK)
        pygame.draw.rect(game_window, GREEN, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        if snake_head in snake_list[:-1]:
            show_game_over()
            return

        draw_snake(snake_list)

        if (
            snake_x < food_x + SNAKE_SIZE and snake_x + SNAKE_SIZE > food_x and
            snake_y < food_y + SNAKE_SIZE and snake_y + SNAKE_SIZE > food_y
        ):
            food_x, food_y = random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
            length_of_snake += 1
            score += 1

        display_score(score)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    game_loop()
