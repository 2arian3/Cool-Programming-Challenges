import logic
import pygame
import pygame_widgets

'''colors'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

'''constants'''
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
BLOCK_SIZE = 250

start_x = (SCREEN_WIDTH - 3 * BLOCK_SIZE) // 2
start_y = (SCREEN_HEIGHT - 3 * BLOCK_SIZE) // 2
board_corners = [(start_x, start_y), (start_x + 3*BLOCK_SIZE, start_y + 3*BLOCK_SIZE)]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption('Tic-Tac-Toe')
x, o = pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5)), pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5))
x.fill(WHITE)
o.fill(WHITE)
screen.fill(WHITE)
pygame.draw.circle(o, RED, (BLOCK_SIZE // 2, BLOCK_SIZE // 2), BLOCK_SIZE // 2 - 5, 2)
pygame.draw.aaline(x, BLACK, (5, 5), (BLOCK_SIZE - 5, BLOCK_SIZE - 5), 1)
pygame.draw.aaline(x, BLACK, (5, BLOCK_SIZE - 5), (BLOCK_SIZE - 5, 5), 1)
pygame.draw.line(screen, BLACK, (start_x, start_y + BLOCK_SIZE), (start_x + 3*BLOCK_SIZE, start_y+BLOCK_SIZE), 2)
pygame.draw.line(screen, BLACK, (start_x, start_y + 2*BLOCK_SIZE), (start_x + 3*BLOCK_SIZE, start_y+2*BLOCK_SIZE), 2)
pygame.draw.line(screen, BLACK, (start_x + BLOCK_SIZE, start_y), (start_x + BLOCK_SIZE, start_y+3*BLOCK_SIZE), 2)
pygame.draw.line(screen, BLACK, (start_x + 2*BLOCK_SIZE, start_y), (start_x + 2*BLOCK_SIZE, start_y+3*BLOCK_SIZE), 2)
pygame.display.update()

'''game loop'''
running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    



