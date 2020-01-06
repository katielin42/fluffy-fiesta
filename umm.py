# #####hardcoded board, will be removed once i know what the FUCKKK im doing.

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
# board = input("input")

def solve(board):

    findE = findEmptyLoc(board)

    if findE:
        r, c = findE
    else:
        return True

    for i in range(1, 10):
        if isValid(board, (r, c), i):
            board[r][c] = i

            if solve(board):
                return True

            board[r][c] = 0

    return False


def isValid(board, position, number):

    #row
    for r in range(len(board)):
        if board[position[0]][r] == number and position[1] != r:
            return False
    #col
    for c in range(len(board)):
        if board[c][position[1]] == number and position[1] != c:
            return False

    #3x3 mat
    xSquare = position[1]//3
    ySquare = position[0]//3

    for r in range(ySquare*3, ySquare*3 + 3):
        for c in range(xSquare*3, xSquare*3 + 3):
            if board[r][c] == number and (r,c) != position:
                return False

    return True

def findEmptyLoc(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return (r, c)
    return None

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")




print_board(board)

