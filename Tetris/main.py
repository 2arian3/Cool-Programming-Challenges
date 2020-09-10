import pygame
import random
from shapes import shapes, colors

pygame.init()

WIDTH        = 800
HEIGHT       = 800
BLOCK_SIZE   = 35
BOARD_WIDTH  = 10 * BLOCK_SIZE
BOARD_HEIGHT = 20 * BLOCK_SIZE
FONT1        = pygame.font.SysFont('FFF phantom 01.ttf', 20)

#Texts used in the game
tetris = FONT1.render('Tetris', True, (255, 0, 0))

start_x = (WIDTH - BOARD_WIDTH) // 2
start_y = (HEIGHT - BOARD_HEIGHT) // 2
cell_colors = [[(10, 0, 0) for _ in range(10)] for _ in range(20)]


def draw_board():
    window.blit(tetris, (start_x + 5*BLOCK_SIZE - tetris.get_width() // 2, 10))
    for i in range(20):
        for j in range(10):
            pygame.draw.rect(window, cell_colors[i][j], (start_x + j*BLOCK_SIZE, start_y + i*BLOCK_SIZE, 35, 35), 0)
    # pygame.draw.rect(window, (255, 255, 255), (start_x, start_y, 10*BLOCK_SIZE, 20*BLOCK_SIZE), 3)
    # for i in range(1, 20):
    #     pygame.draw.line(window, (128, 128, 128), (start_x, start_y + i*BLOCK_SIZE), (start_x + 10*BLOCK_SIZE, start_y + i*BLOCK_SIZE))
    # for i in range(1, 10):
    #     pygame.draw.line(window, (128, 128, 128), (start_x + i*BLOCK_SIZE, start_y), (start_x + i*BLOCK_SIZE, start_y + 20*BLOCK_SIZE))
    pygame.display.update()
     
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TETRIS')
window.fill((0, 0, 0))
draw_board()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


