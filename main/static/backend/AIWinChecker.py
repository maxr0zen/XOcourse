def check_horizontal(board, row, u_type):
    opposed = 'x'
    sign = 'o'
    if u_type == 'min':
        opposed = 'o'
        sign = 'x'
    v = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s row
        if board[row][i] != opposed:
            unfilled += 1
            if board[row][i] == sign:
                v += 1
    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def check_vertical(board, col, u_type):
    opposed = 'x'
    sign = 'o'
    if u_type == 'min':
        opposed = 'o'
        sign = 'x'
    v = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s column
        if board[i][col] != opposed:
            unfilled += 1
            if board[i][col] == sign:
                v += 1
    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def left_diagonal(board, row, col, u_type): # NOTE top_left to bottom_right diagonal check
    opposed = 'x'
    sign = 'o'
    if u_type == 'min':
        opposed = 'o'
        sign = 'x'
    v = 0
    unfilled = 0
    if row == col:
        for i in range(3):
            if board[i][i] != opposed:
                unfilled += 1
                if board[i][i] == sign:
                    v += 1
    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def right_diagonal(board, row, col, u_type):
    opposed = 'x'
    sign = 'o'
    if u_type == 'min':
        opposed = 'o'
        sign = 'x'
    v = 0
    unfilled = 0
    state = False
    for i in range(len(board)):
        if board[i][abs(i-2)] == board[row][col]:
            state = True
        if board[i][abs(i-2)] != opposed:
            unfilled += 1
            if board[i][abs(i-2)] == sign:
                v +=1
    if unfilled == 3 and state == True:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v