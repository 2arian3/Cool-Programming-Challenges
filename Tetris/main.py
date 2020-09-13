import pygame
import random
from shapes import shapes, colors

pygame.init()
screen_info = pygame.display.Info()

#Constants
FPS = 120
WIDTH = 800
HEIGHT = 800 if screen_info.current_h > 1080 else 600
BLOCK_SIZE = 30 if screen_info.current_h > 1080 else 20
BOARD_WIDTH = 10 * BLOCK_SIZE
BOARD_HEIGHT = 20 * BLOCK_SIZE
BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (128, 128, 128)
TEXT_COLOR = (255, 0, 0)
FONT1 = pygame.font.Font('requiries/FFF phantom 01.ttf', 20)
FONT2 = pygame.font.Font('requiries/FFF phantom 01.ttf', 15)
FONT3 = pygame.font.Font('requiries/FFF phantom 01.ttf', 10)


#Texts used in the game
tetris = FONT1.render('Tetris', True, TEXT_COLOR)
next_shape = FONT2.render('next shape', True, TEXT_COLOR)
first_menu_text = FONT1.render('To start the game, press any button', True, TEXT_COLOR)
play_again = FONT2.render('press any button to play again', True, TEXT_COLOR)
producer = FONT3.render('produced by arian boukani', True, TEXT_COLOR)
version = FONT3.render('version 1.0', True, TEXT_COLOR)
you_lost = FONT2.render('you lost :(', True, TEXT_COLOR)
score_text = FONT2.render('score', True, TEXT_COLOR)

score = 0
start_x = (WIDTH - BOARD_WIDTH) // 2
start_y = (HEIGHT - BOARD_HEIGHT) // 2

#Class for each shape used in the game containing their attributes
class Shape:

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0

#After each next shape checks the losing condition
def lost(locked_positions):
    for locked_position in locked_positions:
        if locked_position[1] <= 0:
            return True
    return False

#Creates each shape based on the shapes list in shapes.py module
def shape_handling(shape):
    block_positions = []
    s = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(s):
        row = list(line)
        for j, column in enumerate(row):
            if column == '*':
                block_positions.append((shape.x + j - 2, shape.y + i - 4))
    return block_positions

#Checks whether the next move is legal or not
def valid_move(shape, cell_colors, locked_positions):
    valid_positions = [[(j, i) for j in range(10) if cell_colors[i][j] == (0, 0, 0)] for i in range(20)]
    shape_positions = shape_handling(shape)
    for pos in shape_positions:
        if pos not in valid_positions :
            if pos[0] < 0 or pos[0] >= 10 or pos[1] >= 20 or pos in locked_positions:
                return False
    return True

#Draws the first menu using pygame modules
def draw_first_menu():
    window.blit(tetris, (start_x + 5*BLOCK_SIZE - tetris.get_width() // 2, 10))
    window.blit(first_menu_text, (WIDTH // 2 - first_menu_text.get_width() // 2, HEIGHT // 2 - first_menu_text.get_height() // 2))
    window.blit(producer, (WIDTH // 2 - producer.get_width() // 2, HEIGHT - 2 * producer.get_height()))
    window.blit(version, (WIDTH // 2 - version.get_width() // 2, HEIGHT -  version.get_height()))
    pygame.display.update()

# draws each frame of the game 
def draw_game_menu(cell_colors):
    window.fill((0, 0, 0))
    window.blit(tetris, (start_x + 5*BLOCK_SIZE - tetris.get_width() // 2, 10))
    for i in range(20):
        for j in range(10):
            pygame.draw.rect(window, cell_colors[i][j], (start_x + j*BLOCK_SIZE, start_y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    pygame.draw.rect(window, TEXT_COLOR, (start_x, start_y, 10*BLOCK_SIZE, 20*BLOCK_SIZE), 3)
    for i in range(1, 20):
        pygame.draw.line(window, BORDER_COLOR, (start_x, start_y + i*BLOCK_SIZE), (start_x + 10*BLOCK_SIZE, start_y + i*BLOCK_SIZE))
    for i in range(1, 10):
        pygame.draw.line(window, BORDER_COLOR, (start_x + i*BLOCK_SIZE, start_y), (start_x + i*BLOCK_SIZE, start_y + 20*BLOCK_SIZE))
    window.blit(producer, (WIDTH // 2 - producer.get_width() // 2, HEIGHT - 2 * producer.get_height()))
    window.blit(version, (WIDTH // 2 - version.get_width() // 2, HEIGHT -  version.get_height()))
#Returns a random shape
def get_shape():
    return Shape(5, 0, random.choice(shapes))

#Handling the next shape panel
def draw_next_shape(shape):
    window.blit(next_shape, (BOARD_WIDTH + ((WIDTH - BOARD_WIDTH + start_x)//2 - next_shape.get_width()//2), start_y))
    x = start_x + 11*BLOCK_SIZE 
    y = start_y + BLOCK_SIZE
    for i, line in enumerate(shape.shape[0]):
        row = list(line)
        for j, column in enumerate(row):
            if column is '*':
                pygame.draw.rect(window, shape.color, (x + j*BLOCK_SIZE, y + i*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1), 0)

#Handling the score board panel
def draw_score_panel():
    window.blit(score_text, (start_x // 2 - score_text.get_width() // 2, start_y))
    s = FONT2.render(str(score), True, (255, 0, 0))
    window.blit(s, (start_x // 2 - s.get_width() // 2, start_y + BLOCK_SIZE))

#Generates each cell color after each frame of the game based on locked positions
def generate_cell_colors(locked_positions):
    cell_colors = [[BACKGROUND_COLOR for _ in range(10)] for _ in range(20)]
    for i in range(20):
        for j in range(10):
            if (j, i) in locked_positions:
                cell_colors[i][j] = locked_positions[(j, i)]
    return cell_colors

#Checks each row of the board. if it is full, returns the indices of the full rows
def full_rows(cell_colors):
    full_rows_indices = []
    for line in cell_colors:
        if BACKGROUND_COLOR not in line:
            full_rows_indices.append(cell_colors.index(line))
    return full_rows_indices

#Cleans the full row and shifts the upper rows down
def clean_row(cell_colors, index, locked_positions):
    global score
    score += 10
    updated = dict(((pos[0], pos[1]+1), color) for (pos, color) in locked_positions.items() if pos[1] < index)
    to_be_removed = [cell for cell in locked_positions if cell[1] <= index]
    cell_colors.pop(index)
    new_cells = [BACKGROUND_COLOR for _ in range(10)]
    cell_colors.reverse()
    cell_colors.append(new_cells)
    cell_colors.reverse()
    for cell in to_be_removed:
        try:
            del locked_positions[cell]
        except:
            pass
    locked_positions.update(updated)

#Main menu
def main(): 
    global score
    score = 0
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
        clock.tick(FPS)
        if level_time / 1000 > 4:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005

        if fall_time / 500 >= fall_speed:
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
            full_rows_indices = full_rows(cell_colors)
            if len(full_rows_indices):
                for row in full_rows_indices:
                    clean_row(cell_colors, row, locked_positions)
        if lost(locked_positions):
            running = False
        draw_game_menu(cell_colors)
        draw_next_shape(next_shape)
        draw_score_panel()
        pygame.display.update()

    window.blit(you_lost, (start_x // 2 - you_lost.get_width() // 2, start_y + BOARD_HEIGHT // 2 - you_lost.get_height()))
    window.blit(you_lost, (BOARD_WIDTH + ((WIDTH - BOARD_WIDTH + start_x)//2 - you_lost.get_width()//2), start_y + BOARD_HEIGHT // 2 - you_lost.get_height()))
    window.blit(play_again, (WIDTH // 2 - play_again.get_width() // 2, start_y + 21 * BLOCK_SIZE))
    pygame.display.update()

#First menu graphics
def first_menu():
    draw_first_menu()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                main()

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BACKGROUND_COLOR)
pygame.display.set_caption('TETRIS')

if __name__ == '__main__':
    pygame.mixer.music.load('requiries/Tetris.mp3')
    pygame.mixer.music.play(-1)
    first_menu()

pygame.display.quit()
quit()