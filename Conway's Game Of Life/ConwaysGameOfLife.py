''' Conway's game of life simply visualized by python. '''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class World:
    def __init__(self, size):
        self.board = np.random.randint(2, size = (size, size))
    ''' Animating the board.'''
    def start(self):
        image = None
        started = False
        plt.title("Conway's Game Of Life")
        while self.board.max():
            if not started:
                plt.ion()
                image = plt.imshow(self.board, cm.gray)
                started = True
            else:
                image.set_data(self.board)
            self.board = rules(self.board)
            plt.pause(0.1)

''' Counting the neighboirs of each cell.
    returns an array containing the number of neighbors of each cell.'''
def countingNeighbors(board):
    return (board[:-2, :-2] + board[:-2, 1:-1] + board[:-2, 2:]
    + board[1:-1, :-2] + board[1:-1, 2:] + board[2:, :-2] + board[2:, 1:-1] + board[2:, 2:])

''' Applying the rules on the cells.'''
def rules(board):
    newBoard = np.zeros(board.shape)
    neighbors = countingNeighbors(board)
    survivors = ((neighbors == 2) | (neighbors == 3)) & (board[1:-1, 1:-1] == 1)
    births = (neighbors == 3) & (board[1:-1, 1:-1] == 0)
    newBoard[1:-1,1:-1][births | survivors] = 1
    return newBoard

def main():  
    SIZE = 128
    world = World(SIZE)
    world.start()

if __name__ == '__main__':
    main()




        