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
FONT2        = pygame.font.SysFont('FFF phantom 01.ttf', 15)


#Texts used in the game
tetris = FONT1.render('Tetris', True, (255, 0, 0))
n_shape = FONT2.render('next shape', True, (255, 0, 0))

start_x = (WIDTH - BOARD_WIDTH) // 2
start_y = (HEIGHT - BOARD_HEIGHT) // 2
cell_colors = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

class Shape:

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0
        
def draw_board():
    window.fill((0, 0, 0))
    window.blit(tetris, (start_x + 5*BLOCK_SIZE - tetris.get_width() // 2, 10))
    for i in range(20):
        for j in range(10):
            pygame.draw.rect(window, cell_colors[i][j], (start_x + j*BLOCK_SIZE, start_y + i*BLOCK_SIZE, 35, 35), 0)
    pygame.draw.rect(window, (255, 255, 255), (start_x, start_y, 10*BLOCK_SIZE, 20*BLOCK_SIZE), 3)
    for i in range(1, 20):
        pygame.draw.line(window, (128, 128, 128), (start_x, start_y + i*BLOCK_SIZE), (start_x + 10*BLOCK_SIZE, start_y + i*BLOCK_SIZE))
    for i in range(1, 10):
        pygame.draw.line(window, (128, 128, 128), (start_x + i*BLOCK_SIZE, start_y), (start_x + i*BLOCK_SIZE, start_y + 20*BLOCK_SIZE))
    next_shape(get_shape())
    pygame.display.update()

def get_shape():
    return Shape(5, 0, random.choice(shapes))

def next_shape(shape):
    window.blit(n_shape, (10*BLOCK_SIZE + ((WIDTH - 10*BLOCK_SIZE + start_x)//2 - n_shape.get_width()//2), start_y))
    x = start_x + 11*BLOCK_SIZE 
    y = start_y + BLOCK_SIZE
    for i, line in enumerate(shape.shape[0]):
        row = list(line)
        for j, column in enumerate(row):
            if column is '*':
                pygame.draw.rect(window, shape.color, (x + j*BLOCK_SIZE, y + i*BLOCK_SIZE, 34, 34), 0)

     
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TETRIS')
draw_board()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


