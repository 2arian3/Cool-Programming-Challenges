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
FONT3        = pygame.font.SysFont('FFF phantom 01.ttf', 10)


#Texts used in the game
tetris = FONT1.render('Tetris', True, (255, 0, 0))
next_shape = FONT2.render('next shape', True, (255, 0, 0))
first_menu_text = FONT1.render('To start the game, press any button', True, (255, 0, 0))
producer = FONT3.render('produced by arian boukani', True, (255, 0, 0))
version = FONT3.render('version 1.0', True, (255, 0, 0))

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

def draw_first_menu():
    window.blit(tetris, (start_x + 5*BLOCK_SIZE - tetris.get_width() // 2, 10))
    window.blit(first_menu_text, (WIDTH // 2 - first_menu_text.get_width() // 2, HEIGHT // 2 - first_menu_text.get_height() // 2))
    window.blit(producer, (WIDTH // 2 - producer.get_width() // 2, HEIGHT - 2 * producer.get_height()))
    window.blit(version, (WIDTH // 2 - version.get_width() // 2, HEIGHT -  version.get_height()))
    pygame.display.update()
    
def draw_game_menu():
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
    draw_next_shape(get_shape())
    pygame.display.update()

def get_shape():
    return Shape(5, 0, random.choice(shapes))

def draw_next_shape(shape):
    window.blit(next_shape, (10*BLOCK_SIZE + ((WIDTH - 10*BLOCK_SIZE + start_x)//2 - next_shape.get_width()//2), start_y))
    x = start_x + 11*BLOCK_SIZE 
    y = start_y + BLOCK_SIZE
    for i, line in enumerate(shape.shape[0]):
        row = list(line)
        for j, column in enumerate(row):
            if column is '*':
                pygame.draw.rect(window, shape.color, (x + j*BLOCK_SIZE, y + i*BLOCK_SIZE, 34, 34), 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill((0, 0, 0))
pygame.display.set_caption('TETRIS')

def main():   
    draw_game_menu()
    running = True

    current_shape = get_shape()
    next_shape = get_shape()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def first_menu():
    draw_first_menu()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                main()

if __name__ == '__main__':
    first_menu()