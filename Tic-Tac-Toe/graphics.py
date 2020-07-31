import time
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

'''returns true if the given position is in the board'''
def inTheBoard(position, corners):
    top_left, bottom_right = corners
    return top_left[0] <= position[0] <= bottom_right[0] and top_left[1] <= position[1] <= bottom_right[1]

startX = (SCREEN_WIDTH - 3 * BLOCK_SIZE) // 2
startY = (SCREEN_HEIGHT - 3 * BLOCK_SIZE) // 2
boardCorners = [(startX, startY), (startX + 3*BLOCK_SIZE, startY + 3*BLOCK_SIZE)]

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
pygame.draw.line(screen, BLACK, (startX, startY + BLOCK_SIZE), (startX + 3*BLOCK_SIZE, startY + BLOCK_SIZE), 2)
pygame.draw.line(screen, BLACK, (startX, startY + 2*BLOCK_SIZE), (startX + 3*BLOCK_SIZE, startY + 2*BLOCK_SIZE), 2)
pygame.draw.line(screen, BLACK, (startX + BLOCK_SIZE, startY), (startX + BLOCK_SIZE, startY + 3*BLOCK_SIZE), 2)
pygame.draw.line(screen, BLACK, (startX + 2*BLOCK_SIZE, startY), (startX + 2*BLOCK_SIZE, startY + 3*BLOCK_SIZE), 2)
pygame.display.update()

'''game loop'''
running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        posX, posY = event.pos
        if inTheBoard((posX, posY), boardCorners):
            posX = ((posX - startX) // BLOCK_SIZE) * BLOCK_SIZE + startX
            posY = ((posY - startY) // BLOCK_SIZE) * BLOCK_SIZE + startY
            j, i = (posX - startX) // BLOCK_SIZE, (posY - startY) // BLOCK_SIZE
            if logic.placeIsFree(logic.board, 3*i + j):
                logic.board[3*i + j] = logic.user
                screen.blit(x, (posX + 2, posY + 2))
            pygame.display.update() 
            time.sleep(1)
            cpuMove = logic.cpuMove(logic.board, logic.cpu, logic.user)
            posY = cpuMove // 3
            posX = cpuMove % 3
            screen.blit(o, (startX + posX*BLOCK_SIZE + 2, startY + posY*BLOCK_SIZE + 2))
    pygame.display.update()
    
