from main.static.backend import gamemodes
from main.templates.main import views

winner = ''
boxes = []

winCombinations = [
    [[0, 0], [0, 1], [0, 2]],  # 1 2 3
    [[1, 0], [1, 1], [1, 2]],  # 4 5 6
    [[2, 0], [2, 1], [2, 2]],  # 7 8 9
    [[0, 0], [1, 0], [2, 0]],  # 1 4 7
    [[0, 1], [1, 1], [2, 1]],  # 2 5 8
    [[0, 2], [1, 2], [2, 2]],  # 3 6 9
    [[0, 0], [1, 1], [2, 2]],  # 1 4 9
    [[0, 2], [1, 1], [2, 0]]]  # 3 5 7


def winCheck(board, winCombinations):
    rows = 0
    for combination in winCombinations:
        rows += 1
        if board[combination[0][0]][combination[0][1]] == board[combination[1][0]][combination[1][1]] == \
                board[combination[2][0]][combination[2][1]] and \
                board[combination[0][0]][combination[0][1]] != '' and board[combination[1][0]][combination[1][1]] != ''\
                and board[combination[2][0]][combination[2][1]] != '':
            boxes = winCombinations[rows - 1]
            winner = board[boxes[0][0]][boxes[0][1]]
            print(f'{winner} - WINNER!')
            print(boxes)

            return True
    else:
        return False


def drawCheck(board):
    counter = 0
    for line in board:
        for square in line:
            if square != '':
                counter += 1
    if counter == 9:
        return True, print('draw')
    else:
        return False


board = [['', '', ''],
        ['', '', ''],
        ['', '', '']]


def clear(board):
    board = [['', '', ''],
        ['', '', ''],
        ['', '', '']]
    return board


counter: int = 0


def single(x,y,counter):
    if counter%2 == 0:
        gamemodes.modes.single_x(gamemodes.modes, board, x, y)
    else:
        gamemodes.modes.single_y(gamemodes.modes, board, x, y)
    counter += 1
    return counter
















