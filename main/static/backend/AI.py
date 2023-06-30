import copy as cp
from main.static.backend import AIWinChecker


class Cell:
    def __init__(self, position, location, max_val, min_val):
        self.position = position
        self.location = location  # NOTE this is a list, [0] is row info and [1] is col info
        self.min_val = min_val
        self.max_val = max_val


def generate_cells(board):
    uboard = cp.deepcopy(board)
    for i in range(len(uboard)):
        for j in range(len(uboard[i])):
            if uboard[i][j] != 'x' and uboard[i][j] != 'o':
                uboard[i][j] = Cell(uboard[i][j], [i, j], 0, 0)
                uboard[i][j].max_val = max_val(board, [i, j])
                uboard[i][j].min_val = min_val(board, [i, j])
                # NOTE convert uboard[i][j] into list of maxval and minval from objects
                uboard[i][j] = [uboard[i][j].position, uboard[i][j].max_val, uboard[i][j].min_val]
    return uboard


def max_val(board, location):  # NOTE only generates one max_val by a given location, not entire board
    maxval = 0
    if board[location[0]][location[1]] != 'o' and board[location[0]][location[1]] != 'x':
        maxval += AIWinChecker.check_horizontal(board, location[0], 'max')  # need row
        maxval += AIWinChecker.check_vertical(board, location[1], 'max')  # need column
        # NOTE diagonal check is splitted into left and right diagonal for convienence
        maxval += AIWinChecker.left_diagonal(board, location[0], location[1], 'max')
        maxval += AIWinChecker.right_diagonal(board, location[0], location[1], 'max')

    return maxval


def min_val(board, location):
    minval = 0
    if board[location[0]][location[1]] != 'o' and board[location[0]][location[1]] != 'x':
        minval -= AIWinChecker.check_horizontal(board, location[0], 'min')
        minval -= AIWinChecker.check_vertical(board, location[1], 'min')
        minval -= AIWinChecker.left_diagonal(board, location[0], location[1], 'min')
        minval -= AIWinChecker.right_diagonal(board, location[0], location[1], 'min')

    return minval



def AI(board, sidebot):
    AIOutput = generate_cells(board)
    toChoose = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    indexCounter = 0
    for index in AIOutput:
        itemCounter = 0
        if index == 'x' or index == 'o':
            pass
        for item in index:

            if len(item) > 2:
                if item[1] > 2:
                    toChoose[indexCounter][itemCounter] = item[1]
                    pass
            for smth in item:
                print('item - ',item)
                if len(item) > 2:

                    if smth == '':
                            smth = 0

                    print('smth - ', smth)
                    print('toshose',toChoose)
                    toChoose[indexCounter][itemCounter] += abs(smth)
            itemCounter += 1
        indexCounter += 1
    maxIndex = [0, 0]
    counter = 0
    maxValue = 0
    for cell in toChoose:
        currentValue = max(cell)
        currentMax = cell.index(currentValue)
        if currentValue > maxValue:
            maxValue = currentValue
            maxIndex = [counter, currentMax]
        counter += 1

    board[maxIndex[0]][maxIndex[1]] = sidebot

    print(maxIndex)
    [print(i) for i in toChoose]
    [print(i) for i in AIOutput]

