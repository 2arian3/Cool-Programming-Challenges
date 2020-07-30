def placeIsFree(board, position):
    return board[position] == ''

def boardIsFull(board):
    return board.count('') == 0

def playerIsWinner(board, player):
    startingPositions = [0, 3, 6]
    for start in startingPositions:
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    startingPositions = [0, 1, 2]
    for start in startingPositions:
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    return (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player)

board = [''] * 9
user = 'x'
cpu = 'o'
print(board.count(''))