import pygame
import random
from shapes import shapes

pygame.init()

WIDTH        = 800
HEIGHT       = 800
BLOCK_SIZE   = 35
BOARD_WIDTH  = 10 * BLOCK_SIZE
BOARD_HEIGHT = 20 * BLOCK_SIZE

start_x = (WIDTH - BOARD_WIDTH) // 2
start_y = (HEIGHT - BOARD_HEIGHT) // 2


def draw_board():
    for i in range(21):
        pygame.draw.line(window, (128, 128, 128), (start_x, start_y + i*BLOCK_SIZE), (start_x + 10*BLOCK_SIZE, start_y + i*BLOCK_SIZE))
    for i in range(11):
        pygame.draw.line(window, (128, 128, 128), (start_x + i*BLOCK_SIZE, start_y), (start_x + i*BLOCK_SIZE, start_y + 20*BLOCK_SIZE))
    pygame.display.update()
     
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TETRIS')
draw_board()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


