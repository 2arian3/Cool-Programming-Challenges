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
SECOND_COLOR     = PINK
X_COLOR          = BLACK
O_COLOR          = RED
GAME_FONT_40     = pygame.font.SysFont('Debussy.ttf', 40)
GAME_FONT_30     = pygame.font.SysFont('Debussy.ttf', 30)

'''texts'''
header = GAME_FONT_40.render('TIC TAC TOE', True, SECOND_COLOR, BACKGROUND_COLOR)
choice = GAME_FONT_30.render('Choose between x and o !', True, SECOND_COLOR, BACKGROUND_COLOR)
hint = GAME_FONT_30.render('HINT : In order to reset the board in the game press return.', True, SECOND_COLOR, BACKGROUND_COLOR)
userTurn = GAME_FONT_30.render('It\'s your turn to move', True, SECOND_COLOR, BACKGROUND_COLOR)
cpuTurn = GAME_FONT_30.render('It\'s cpu\'s turn to move', True, SECOND_COLOR, BACKGROUND_COLOR)
youWon = GAME_FONT_30.render('YOU  WON!', True, SECOND_COLOR, BACKGROUND_COLOR)
youLost = GAME_FONT_30.render('YOU  LOST:(', True, SECOND_COLOR, BACKGROUND_COLOR)
tie = GAME_FONT_30.render('TIE...', True, SECOND_COLOR, BACKGROUND_COLOR)
restart = GAME_FONT_30.render('Wanna  play?  press return.', True, SECOND_COLOR, BACKGROUND_COLOR)

'''returns true if the given position is in the board.'''
def inTheBoard(position):
    top_left, bottom_right = BOARD_CORNERS
    return top_left[0] <= position[0] <= bottom_right[0] and top_left[1] <= position[1] <= bottom_right[1]

'''drawing the board based on the constants.'''
def drawBoard(screen):
    pygame.draw.line(screen, SECOND_COLOR, (START_X, START_Y + BLOCK_SIZE), (START_X + 3*BLOCK_SIZE, START_Y + BLOCK_SIZE), 3)
    pygame.draw.line(screen, SECOND_COLOR, (START_X, START_Y + 2*BLOCK_SIZE), (START_X + 3*BLOCK_SIZE, START_Y + 2*BLOCK_SIZE), 3)
    pygame.draw.line(screen, SECOND_COLOR, (START_X + BLOCK_SIZE, START_Y), (START_X + BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)
    pygame.draw.line(screen, SECOND_COLOR, (START_X + 2*BLOCK_SIZE, START_Y), (START_X + 2*BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)

'''clearing the screen.'''
def clearTheScreen():
    blank = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - 100))
    blank.fill(BACKGROUND_COLOR)
    screen.blit(blank, (0, 75))
    pygame.display.update()

'''clears the board on the screen.'''
def resetTheBoard(screen):
    logic.board = [''] * 9
    blank = pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5))
    blank.fill(BACKGROUND_COLOR)
    for i in range(3):
        for j in range(3):
            screen.blit(blank, (START_X + i*BLOCK_SIZE + 2, START_Y + j*BLOCK_SIZE + 2))

'''creating the players icons.'''
def creatingTheIcons():
    x, o = pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5)), pygame.Surface((BLOCK_SIZE-5, BLOCK_SIZE-5))
    x.fill(BACKGROUND_COLOR)
    o.fill(BACKGROUND_COLOR)
    pygame.draw.circle(o, O_COLOR, (BLOCK_SIZE // 2, BLOCK_SIZE // 2), BLOCK_SIZE // 2 - 5, 2)
    pygame.draw.aaline(x, X_COLOR, (5, 5), (BLOCK_SIZE - 5, BLOCK_SIZE - 5), 1)
    pygame.draw.aaline(x, X_COLOR, (5, BLOCK_SIZE - 5), (BLOCK_SIZE - 5, 5), 1)
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
        logic.board[3*i + j] = USER
        screen.blit(playerIcon, (posX + 2, posY + 2))
        legal = True
    pygame.display.update()
    return legal

'''cpu's move appears on the board.'''
def cpuMove(screen):
    move = logic.cpuMove(logic.board, CPU, USER)
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
    choiceRect = choice.get_rect()
    choiceRect.center = ((SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 - 100))
    hintRect = hint.get_rect()
    hintRect.center = ((SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
    xButton = Button(
            screen, (SCREEN_WIDTH-50)//2-50, (SCREEN_HEIGHT-50)//2, 50, 50, text='X',
            fontSize=30, margin=20,
            font=GAME_FONT_30,
            textColour=SECOND_COLOR,
            inactiveColour=BACKGROUND_COLOR,
            pressedColour=SECOND_COLOR, radius=5,
            onClick=lambda: chooseIcon('X')
         )
    oButton = Button(
            screen, (SCREEN_WIDTH-50)//2+50, (SCREEN_HEIGHT-50)//2, 50, 50, text='O',
            fontSize=30, margin=20,
            font=GAME_FONT_30,
            textColour=SECOND_COLOR,
            inactiveColour=BACKGROUND_COLOR,
            pressedColour=SECOND_COLOR, radius=5,
            onClick=lambda: chooseIcon('O')
         ) 
    screen.blit(choice, choiceRect)
    screen.blit(hint, hintRect)
    while USER is '':
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        oButton.listen(events)
        xButton.listen(events)
        oButton.draw()
        xButton.draw()
        pygame.display.update()
    clearTheScreen()

def showTurn(screen, player):
    turn = userTurn if player == USER else cpuTurn
    turnRect = turn.get_rect()
    turnRect.center = ((SCREEN_WIDTH // 2, 100))
    screen.blit(turn, turnRect)
    pygame.display.update()

def eraseTurn(screen):
    blank = pygame.Surface((SCREEN_WIDTH, 50))
    blank.fill(BACKGROUND_COLOR)
    blankRect = blank.get_rect()
    blankRect.center = ((SCREEN_WIDTH // 2, 100))
    screen.blit(blank, blankRect)
    pygame.display.update()

def roundFinished(winner=None):
    restartRect = restart.get_rect()
    restartRect.center = ((SCREEN_WIDTH // 2, SCREEN_WIDTH - 100))
    screen.blit(restart, restartRect)
    textToBeShown = youWon if winner == USER else (youLost if winner == CPU else tie)
    textRect = textToBeShown.get_rect()
    textRect.center = ((SCREEN_WIDTH // 2, 100))
    screen.blit(textToBeShown, textRect)
    running = True
    pygame.display.update()
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            running = False
        pygame.display.update()
    clearTheScreen()
    time.sleep(1)
    drawBoard(screen)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    screen.fill(BACKGROUND_COLOR)
    pygame.display.set_caption('Tic-Tac-Toe')
    headerRect = header.get_rect()
    headerRect.center = ((SCREEN_WIDTH // 2, 50))
    screen.blit(header, headerRect)
    intro(screen)
    drawBoard(screen)
    x, o = creatingTheIcons()
    pygame.display.update()

    '''game loop'''
    running = True
    winner = ''
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        showTurn(screen, USER)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = event.pos
            if inTheBoard((posX, posY)):
                if playerMove(screen, (posX, posY)):
                    if logic.playerIsWinner(logic.board, USER):
                        eraseTurn(screen)
                        roundFinished(USER)
                    elif logic.boardIsFull(logic.board):
                        eraseTurn(screen)
                        roundFinished()
                    else:
                        eraseTurn(screen)
                        showTurn(screen, CPU)
                        time.sleep(2)
                        cpuMove(screen)
                        if logic.playerIsWinner(logic.board, CPU):
                            eraseTurn(screen)
                            roundFinished(CPU)
                        else:
                            eraseTurn(screen)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            resetTheBoard(screen)
        pygame.display.update()

if __name__ == '__main__':
    main()

pygame.quit()