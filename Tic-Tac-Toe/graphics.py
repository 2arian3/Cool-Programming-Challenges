import time
import logic
import pygame
from pygame_widgets import Button
pygame.init()

'''colors'''
#              R    G    B
BLACK      = (  0,   0,   0)
RED        = (255,   0,   0)
GREEN      = (124, 209,  65)
DARK_BLUE  = ( 16,  34,  60)
PINK       = (255,  20, 147)
BLUE       = (152, 244, 245)
YELLOW     = (248, 241,  87)

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
X_COLOR          = BLUE
O_COLOR          = PINK
BOARD_COLOR      = YELLOW
GAME_FONT_40     = pygame.font.SysFont('Debussy.ttf', 40)
GAME_FONT_30     = pygame.font.SysFont('Debussy.ttf', 30)

'''texts'''
header   = GAME_FONT_40.render('TIC TAC TOE', True, BLUE, BACKGROUND_COLOR)
choice   = GAME_FONT_30.render('Choose between x and o !', True, PINK, BACKGROUND_COLOR)
hint     = GAME_FONT_30.render('HINT : In order to reset the board in the game press return.', True, PINK, BACKGROUND_COLOR)
userTurn = GAME_FONT_30.render('It is your turn to move', True, BLUE, BACKGROUND_COLOR)
cpuTurn  = GAME_FONT_30.render('It is cpu\'s turn to move', True, BLUE, BACKGROUND_COLOR)
youWon   = GAME_FONT_30.render('YOU  WON!', True, BLUE, BACKGROUND_COLOR)
youLost  = GAME_FONT_30.render('YOU  LOST:(', True, BLUE, BACKGROUND_COLOR)
tie      = GAME_FONT_30.render('TIE...', True, BLUE, BACKGROUND_COLOR)
restart  = GAME_FONT_30.render('Wanna  play?  press return.', True, BLUE, BACKGROUND_COLOR)

'''returns true if the given position is in the board.'''
def inTheBoard(position):
    top_left, bottom_right = BOARD_CORNERS
    return top_left[0] <= position[0] <= bottom_right[0] and top_left[1] <= position[1] <= bottom_right[1]

'''drawing the board based on the constants.'''
def drawBoard():
    pygame.draw.line(screen, BOARD_COLOR, (START_X, START_Y), (START_X + 3*BLOCK_SIZE, START_Y), 3)
    pygame.draw.line(screen, BOARD_COLOR, (START_X, START_Y), (START_X, START_Y + 3*BLOCK_SIZE), 3)
    pygame.draw.line(screen, BOARD_COLOR, (START_X + 3*BLOCK_SIZE, START_Y), (START_X + 3*BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)
    pygame.draw.line(screen, BOARD_COLOR, (START_X, START_Y + BLOCK_SIZE), (START_X + 3*BLOCK_SIZE, START_Y + BLOCK_SIZE), 3)
    pygame.draw.line(screen, BOARD_COLOR, (START_X, START_Y + 2*BLOCK_SIZE), (START_X + 3*BLOCK_SIZE, START_Y + 2*BLOCK_SIZE), 3)
    pygame.draw.line(screen, BOARD_COLOR, (START_X + BLOCK_SIZE, START_Y), (START_X + BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)
    pygame.draw.line(screen, BOARD_COLOR, (START_X + 2*BLOCK_SIZE, START_Y), (START_X + 2*BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)
    pygame.draw.line(screen, BOARD_COLOR, (START_X, START_Y + 3*BLOCK_SIZE), (START_X + 3*BLOCK_SIZE, START_Y + 3*BLOCK_SIZE), 3)

'''clearing the screen.'''
def clearTheScreen():
    blank = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - 100))
    blank.fill(BACKGROUND_COLOR)
    screen.blit(blank, (0, 75))
    pygame.display.update()

'''clears the board on the screen.'''
def resetTheBoard():
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
    pygame.draw.circle(o, O_COLOR, (BLOCK_SIZE // 2, BLOCK_SIZE // 2), BLOCK_SIZE // 2 - 5, 3)
    pygame.draw.aaline(x, X_COLOR, (5, 5), (BLOCK_SIZE - 5, BLOCK_SIZE - 5), 3)
    pygame.draw.aaline(x, X_COLOR, (5, BLOCK_SIZE - 5), (BLOCK_SIZE - 5, 5), 3)
    return x, o

'''visualizing player's move.'''
def playerMove(position):
    legal = False
    playerIcon = x if USER == 'X' else o
    posX, posY = position
    posX = ((posX - START_X) // BLOCK_SIZE) * BLOCK_SIZE + START_X
    posY = ((posY - START_Y) // BLOCK_SIZE) * BLOCK_SIZE + START_Y
    j, i = (posX - START_X) // BLOCK_SIZE, (posY - START_Y) // BLOCK_SIZE
    if logic.placeIsFree(3*i + j):
        logic.board[3*i + j] = USER
        screen.blit(playerIcon, (posX + 2, posY + 2))
        legal = True
    pygame.display.update()
    return legal

'''cpu's move appears on the board.'''
def cpuMove():
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
def intro():
    choiceRect = choice.get_rect()
    choiceRect.center = ((SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 - 100))
    hintRect = hint.get_rect()
    hintRect.center = ((SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
    xButton = Button(
            screen, (SCREEN_WIDTH-50)//2-50, (SCREEN_HEIGHT-50)//2, 50, 50, text='X',
            fontSize=30, margin=20,
            font=GAME_FONT_30,
            textColour=PINK,
            inactiveColour=BACKGROUND_COLOR,
            pressedColour=PINK, radius=5,
            onClick=lambda: chooseIcon('X')
         )
    oButton = Button(
            screen, (SCREEN_WIDTH-50)//2+50, (SCREEN_HEIGHT-50)//2, 50, 50, text='O',
            fontSize=30, margin=20,
            font=GAME_FONT_30,
            textColour=PINK,
            inactiveColour=BACKGROUND_COLOR,
            pressedColour=PINK, radius=5,
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

def showTurn(player):
    turn = userTurn if player == USER else cpuTurn
    turnRect = turn.get_rect()
    turnRect.center = ((SCREEN_WIDTH // 2, 100))
    screen.blit(turn, turnRect)
    pygame.display.update()

def eraseTurn():
    blank = pygame.Surface((SCREEN_WIDTH, 50))
    blank.fill(BACKGROUND_COLOR)
    blankRect = blank.get_rect()
    blankRect.center = ((SCREEN_WIDTH // 2, 100))
    screen.blit(blank, blankRect)
    pygame.display.update()
def winningLine(winner):
    scenarios = {
        (0, 1, 2) : [(START_X, START_Y+BLOCK_SIZE//2), (START_X+3*BLOCK_SIZE, START_Y+BLOCK_SIZE//2)],
        (3, 4, 5) : [(START_X, START_Y+BLOCK_SIZE+BLOCK_SIZE//2), (START_X+3*BLOCK_SIZE, START_Y+BLOCK_SIZE+BLOCK_SIZE//2)],
        (6, 7, 8) : [(START_X, START_Y+2*BLOCK_SIZE+BLOCK_SIZE//2), (START_X+3*BLOCK_SIZE, START_Y+2*BLOCK_SIZE+BLOCK_SIZE//2)],
        (0, 3, 6) : [(START_X+BLOCK_SIZE//2, START_Y), (START_X+BLOCK_SIZE//2, START_Y+3*BLOCK_SIZE)],
        (1, 4, 7) : [(START_X+BLOCK_SIZE+BLOCK_SIZE//2, START_Y), (START_X+BLOCK_SIZE+BLOCK_SIZE//2, START_Y+3*BLOCK_SIZE)],
        (2, 5, 8) : [(START_X+2*BLOCK_SIZE+BLOCK_SIZE//2, START_Y), (START_X+2*BLOCK_SIZE+BLOCK_SIZE//2, START_Y+3*BLOCK_SIZE)],
        (0, 4, 8) : [(START_X, START_Y), (START_X+3*BLOCK_SIZE, START_Y+3*BLOCK_SIZE)],
        (2, 4, 6) : [(START_X+3*BLOCK_SIZE, START_Y), (START_X, 3*START_Y+BLOCK_SIZE)]
    }
    scenario = ''
    for i in [0, 3, 6]:
        if logic.board[i] == logic.board[i+1] == logic.board[i+2] == winner:
            scenario = (i, i+1, i+2)
            break
    for i in [0, 1, 2]:
        if logic.board[i] == logic.board[i+3] == logic.board[i+6] == winner:
            scenario = (i, i+3, i+6)
            break
    if logic.board[0] == logic.board[4] == logic.board[8] == winner:
        scenario = (0, 4, 8) 
    if logic.board[2] == logic.board[4] == logic.board[6] == winner:
        scenario = (2, 4, 6)
    scenario = scenarios.get(scenario)
    pygame.draw.line(screen, RED, scenario[0], scenario[1], 3)
    pygame.display.update()

def roundFinished(winner=None):
    restartRect = restart.get_rect()
    restartRect.center = ((SCREEN_WIDTH // 2, SCREEN_WIDTH - 100))
    screen.blit(restart, restartRect)
    textToBeShown = youWon if winner == USER else (youLost if winner == CPU else tie)
    if winner is not None:
        winningLine(winner)
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
    drawBoard()
    resetTheBoard()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Tic-Tac-Toe')
x, o = creatingTheIcons()

def main():
    headerRect = header.get_rect()
    headerRect.center = ((SCREEN_WIDTH // 2, 50))
    screen.blit(header, headerRect)
    intro()
    drawBoard()
    pygame.display.update()

    '''game loop'''
    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        showTurn(USER)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = event.pos
            if inTheBoard((posX, posY)):
                if playerMove((posX, posY)):
                    if logic.playerIsWinner(logic.board, USER):
                        eraseTurn()
                        roundFinished(USER)
                    elif logic.boardIsFull():
                        eraseTurn()
                        roundFinished()
                    else:
                        eraseTurn()
                        showTurn(CPU)
                        time.sleep(1.5)
                        cpuMove()
                        if logic.playerIsWinner(logic.board, CPU):
                            eraseTurn()
                            roundFinished(CPU)
                        else:
                            eraseTurn()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            resetTheBoard()
        pygame.display.update()

if __name__ == '__main__':
    main()

pygame.quit()