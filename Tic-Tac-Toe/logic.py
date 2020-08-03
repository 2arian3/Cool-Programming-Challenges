'''returns true if the given position in the board is free.'''
def placeIsFree(position):
    return board[position] == ''

'''returns true if the board is full.'''
def boardIsFull():
    return board.count('') == 0

'''checks all the possibilities of the winning and returns true if one of the conditions is satisfied.'''
def playerIsWinner(board, player):
    startingPositions = [0, 3, 6]
    for start in startingPositions:
        if board[start] == board[start+1] == board[start+2] == player:
            return True
    startingPositions = [0, 1, 2]
    for start in startingPositions:
        if board[start] == board[start+3] == board[start+6] == player:
            return True
    return (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player)

'''cpu moves based on some simple rules. don't worry it's not unbeatable:))'''
def cpuMove(board, cpu, user):
    import random
    corners = [0, 2, 6, 8]
    legalMoves = [x for x in range(9) if board[x] is '']
    legalCorners = [x for x in corners if x in legalMoves]
    for move in legalMoves:
        tempBoard = board.copy() 
        tempBoard[move] = cpu
        if playerIsWinner(tempBoard, cpu):
            board[move] = cpu
            return move
    for move in legalMoves:
        tempBoard = board.copy() 
        tempBoard[move] = user
        if playerIsWinner(tempBoard, user):
            board[move] = cpu
            return move
    if board[4] == '':
        board[4] = cpu
        return 4
    move = -1
    if len(legalCorners):
        move = random.choice(legalCorners)
    else:
        move = random.choice(legalMoves)
    board[move] = cpu
    return move

board = [''] * 9