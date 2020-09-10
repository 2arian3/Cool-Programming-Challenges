import pygame
import random
from shapes import shapes, colors

pygame.init()

#Constants
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
you_lost = FONT2.render('you lost :(', True, (255, 0, 0))

score = 0
start_x = (WIDTH - BOARD_WIDTH) // 2
start_y = (HEIGHT - BOARD_HEIGHT) // 2

class Shape:

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0

def lost(locked_positions):
    for locked_position in locked_positions:
        if locked_position[1] <= 0:
            return True
    return False

def shape_handling(shape):
    block_positions = []
    s = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(s):
        row = list(line)
        for j, column in enumerate(row):
            if column == '*':
                block_positions.append((shape.x + j - 2, shape.y + i - 4))
    return block_positions

def valid_move(shape, cell_colors, locked_positions):
    valid_positions = [[(j, i) for j in range(10) if cell_colors[i][j] == (0, 0, 0)] for i in range(20)]
    shape_positions = shape_handling(shape)
    for pos in shape_positions:
        if pos not in valid_positions :
            if pos[0] < 0 or pos[0] >= 10 or pos[1] >= 20 or pos in locked_positions:
                return False
    return True

def draw_first_menu():
    window.blit(tetris, (start_x + 5*BLOCK_SIZE - tetris.get_width() // 2, 10))
    window.blit(first_menu_text, (WIDTH // 2 - first_menu_text.get_width() // 2, HEIGHT // 2 - first_menu_text.get_height() // 2))
    window.blit(producer, (WIDTH // 2 - producer.get_width() // 2, HEIGHT - 2 * producer.get_height()))
    window.blit(version, (WIDTH // 2 - version.get_width() // 2, HEIGHT -  version.get_height()))
    pygame.display.update()
    
def draw_game_menu(cell_colors):
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

def generate_cell_colors(locked_positions):
    cell_colors = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for i in range(20):
        for j in range(10):
            if (j, i) in locked_positions:
                cell_colors[i][j] = locked_positions[(j, i)]
    return cell_colors

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill((0, 0, 0))
pygame.display.set_caption('TETRIS')

def main(): 
    locked_positions = dict()  
    cell_colors = generate_cell_colors(locked_positions)
    running = True
    next_move = False
    current_shape = get_shape()
    next_shape = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    fall_speed = 0.3
    draw_game_menu(cell_colors)

    while running:

        cell_colors = generate_cell_colors(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        if level_time / 1000 > 4:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_shape.y += 1
            if not (valid_move(current_shape, cell_colors, locked_positions)) and current_shape.y > 0:
                current_shape.y -= 1
                next_move = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_shape.x -= 1
                    if not valid_move(current_shape, cell_colors, locked_positions):
                        current_shape.x += 1
                
                elif event.key == pygame.K_RIGHT:
                    current_shape.x += 1
                    if not valid_move(current_shape, cell_colors, locked_positions):
                        current_shape.x -= 1
                
                elif event.key == pygame.K_DOWN:
                    current_shape.y += 1
                    if not valid_move(current_shape, cell_colors, locked_positions):
                        current_shape.y -= 1

                elif event.key == pygame.K_UP:
                    current_shape.rotation = current_shape.rotation + 1 % len(current_shape.shape)
                    if not valid_move(current_shape, cell_colors, locked_positions):
                        current_shape.rotation = current_shape.rotation - 1 % len(current_shape.shape)
        shape_positions = shape_handling(current_shape)
        for x, y in shape_positions:
            if y >= 0:
                cell_colors[y][x] = current_shape.color
        if next_move:
            for pos in shape_positions:
                locked_positions[pos] = current_shape.color
            current_shape = next_shape
            next_shape = get_shape()
            next_move = False
        if lost(locked_positions):
            running = False
        draw_game_menu(cell_colors)
        draw_next_shape(next_shape)
        pygame.display.update()

    window.blit(you_lost, (start_x // 2 - you_lost.get_width() // 2, start_y))
    pygame.display.update()
    pygame.time.delay(3000)

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

pygame.display.quit()
quit()