# Este código é um exemplo simples de um jogo da cobra (Snake) implementado em Python usando a biblioteca Pygame.

# Inicialização do Pygame:
#
# pygame.init(): Inicializa o Pygame, preparando-o para o uso.
# Definição de Cores e Tamanho da Tela:
#
# white, red, black: São tuplas de cores em formato RGB.
# screen_width, screen_height: Definem as dimensões da tela do jogo.
# Configuração da Janela do Jogo:
#
# gamewind = pygame.display.set_mode((screen_width, screen_height)): Cria a janela do jogo com as dimensões especificadas.
# Configuração da Fonte e Relógio:
#
# font = pygame.font.SysFont(None, 35): Define a fonte e tamanho do texto.
# clock = pygame.time.Clock(): Cria um objeto para controlar a taxa de quadros por segundo (FPS) do jogo.
# Funções Auxiliares:
#
# text_screen(text, color, x, y): Renderiza e exibe um texto na tela.
# plot_snake(gamewind, color, snk_list, snake_size): Desenha a cobra na tela.
# Configuração Inicial da Cobra e Comida:
#
# snake_list: Lista que armazena as posições da cobra.
# length_of_snake: Comprimento inicial da cobra.
# snake_size: Tamanho dos blocos que compõem a cobra.
# init_velocity: Velocidade inicial da cobra.
# snake_x, snake_y: Posição inicial da cabeça da cobra.
# food_x, food_y: Posição inicial da comida.
# score: Pontuação do jogador.
# fps: Taxa de quadros por segundo.
# Loop Principal do Jogo:
#
# while not exit_game:: Loop principal que executa o jogo até que o jogador decida sair.
# Verifica eventos do teclado para controlar a direção da cobra.
# Move a cobra e verifica colisões com as bordas da tela.
# Desenha a cobra, a comida e a pontuação na tela.
# Verifica se a cobra colide com a comida, atualiza a posição da comida e aumenta a pontuação.
# Atualiza a tela e controla a taxa de quadros.
# Finalização do Jogo:
#
# pygame.quit(), quit(): Finaliza o Pygame e encerra o programa quando o loop é encerrado.
# O jogo termina se a cabeça da cobra colidir com as bordas da tela ou com o próprio corpo.
# A pontuação aumenta cada vez que a cobra come a comida. O jogador pode controlar a cobra usando as teclas de seta.