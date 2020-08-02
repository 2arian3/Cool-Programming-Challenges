import time
import logic
import pygame
from pygame_widgets import Button
pygame.init()

'''colors'''
#              R    G    B
BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
RED        = (255,   0,   0)
GREEN      = (124, 209,  65)
DARK_BLUE  = ( 26,  38,  95)
PINK       = (255,  20, 147)
BLUE       = ( 54, 123, 201)

'''constants'''
USER             = ''
CPU              = ''
SCREEN_WIDTH     = 1000
SCREEN_HEIGHT    = 1000
BLOCK_SIZE       = 200
START_X          = (SCREEN_WIDTH - 3 * BLOCK_SIZE) // 2
START_Y          = (SCREEN_HEIGHT - 3 * BLOCK_SIZE) // 2
BOARD_CORNERS    = [(START_X, START_Y), (START_X + 3*BLOCK_SIZE, START_Y + 3*BLOCK_SIZE)]
BACKGROUND_COLOR = DARK_BLUE
GAME_FONT_40     = pygame.font.SysFont('Debussy.ttf', 40)
GAME_FONT_30     = pygame.font.SysFont('Debussy.ttf', 30)

'''returns true if the given position is in the board.'''
def inTheBoard(position):
    top_left, bottom_right = BOARD_CORNERS
    return top_left[0] <= position[0] <= bottom_right[0] and top_left[1] <= position[1] <= bottom_right[1]

'''drawing the board based on the constants.'''
def drawBoard(screen):
    pygame.draw.line(screen, PINK, (START_X, START_Y + BLOCK_SIZE), (START_X + 3*BLOCK_SIZE, START_Y + BLOCK_SIZE), 3)
    pygame.draw.line(screen, PINK, (START_X, START_Y + 2*BLOCK_SIZE), (START_X + 3*BLOCK_SIZE, START_Y + 2*BLOCK_SIZE), 3)
    pygame.draw.line(screen, PINK, (START_X + BLOCK_SIZE, START_Y), (START_X + BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)
    pygame.draw.line(screen, PINK, (START_X + 2*BLOCK_SIZE, START_Y), (START_X + 2*BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)

'''clears the board on the screen.'''
def resetTheBoard(screen):
    logic.board = [''] * 9
    blank = pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5))
    blank.fill(BACKGROUND_COLOR)
    for i in range(3):
        for j in range(3):
            screen.blit(blank, (START_X + i*BLOCK_SIZE + 2, START_Y + j*BLOCK_SIZE + 2))

'''creating the players icons.'''
def creatingTheIcons(xColor, oColor):
    x, o = pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5)), pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5))
    x.fill(BACKGROUND_COLOR)
    o.fill(BACKGROUND_COLOR)
    pygame.draw.circle(o, oColor, (BLOCK_SIZE // 2, BLOCK_SIZE // 2), BLOCK_SIZE // 2 - 5, 2)
    pygame.draw.aaline(x, xColor, (5, 5), (BLOCK_SIZE - 5, BLOCK_SIZE - 5), 1)
    pygame.draw.aaline(x, xColor, (5, BLOCK_SIZE - 5), (BLOCK_SIZE - 5, 5), 1)
    return x, o

'''visualizing player's move.'''
def playerMove(screen, position):
    legal = False
    playerIcon = x if USER == 'X' else o
    posX, posY = position
    posX = ((posX - START_X) // BLOCK_SIZE) * BLOCK_SIZE + START_X
    posY = ((posY - START_Y) // BLOCK_SIZE) * BLOCK_SIZE + START_Y
    j, i = (posX - START_X) // BLOCK_SIZE, (posY - START_Y) // BLOCK_SIZE
    if logic.placeIsFree(logic.board, 3*i + j):
        logic.board[3*i + j] = logic.user
        screen.blit(playerIcon, (posX + 2, posY + 2))
        legal = True
    pygame.display.update()
    return legal

'''cpu's move appears on the board.'''
def cpuMove(screen):
    move = logic.cpuMove(logic.board, logic.cpu, logic.user)
    cpuIcon = x if CPU == 'X' else o
    posY = move // 3
    posX = move % 3
    screen.blit(cpuIcon, (START_X + posX*BLOCK_SIZE + 2, START_Y + posY*BLOCK_SIZE + 2))
    pygame.display.update()

def chooseIcon(icon):
    global USER
    global CPU
    USER = icon
    CPU = 'O' if icon == 'X' else 'X'

'''the intro screen.'''
def intro(screen):
    choice = GAME_FONT_30.render('Choose between x and o !', True, PINK, DARK_BLUE)
    choiceRect = choice.get_rect()
    choiceRect.center = ((SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 - 100))
    xButton = Button(
            screen, (SCREEN_WIDTH-50)//2+50, (SCREEN_HEIGHT-50)//2, 50, 50, text='X',
            fontSize=30, margin=20,
            font=GAME_FONT_30,
            textColour=PINK,
            inactiveColour=BACKGROUND_COLOR,
            pressedColour=PINK, radius=5,
            onClick=lambda: chooseIcon('X')
         )
    oButton = Button(
            screen, (SCREEN_WIDTH-50)//2-50, (SCREEN_HEIGHT-50)//2, 50, 50, text='O',
            fontSize=30, margin=20,
            font=GAME_FONT_30,
            textColour=PINK,
            inactiveColour=BACKGROUND_COLOR,
            pressedColour=PINK, radius=5,
            onClick=lambda: chooseIcon('O')
         ) 
    screen.blit(choice, choiceRect)
    while USER is '':
        events = pygame.event.get()
        oButton.listen(events)
        xButton.listen(events)
        oButton.draw()
        xButton.draw()
        pygame.display.update()
    blank = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - 100))
    blank.fill(BACKGROUND_COLOR)
    screen.blit(blank, (0, 100))
    pygame.display.update()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Tic-Tac-Toe')
header = GAME_FONT_40.render('TIC TAC TOE', True, PINK, DARK_BLUE)
headerRect = header.get_rect()
headerRect.center = ((SCREEN_WIDTH // 2, 50))
screen.blit(header, headerRect)
# userTurn = gameFont30.render('It\'s your turn to move', True, PINK, DARK_BLUE)
# cpuTurn = gameFont30.render('It\'s cpu\'s turn to move', True, PINK, DARK_BLUE)
intro(screen)
drawBoard(screen)
x, o = creatingTheIcons(BLACK, RED)
pygame.display.update()

'''game loop'''
running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        posX, posY = event.pos
        if inTheBoard((posX, posY)):
            if playerMove(screen, (posX, posY)):
                time.sleep(1)
                cpuMove(screen)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        resetTheBoard(screen)
    pygame.display.update()