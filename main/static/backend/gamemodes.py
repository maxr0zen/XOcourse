import random
from main.static.backend import AI
from main.templates.main.views import *
from main.static.backend import main


class modes:

    def __init__(self, x, y, last):
        self.x = x
        self.y = y
        self.last = last

    def singlePlay(self, board, winCombinations, x, y, counter):
        print(counter, ' - counter')
        print('запущено')
        [print(i) for i in board]
        if main.counter % 2 == 0:
            last = 'x'
        else:
            last = 'o'
        if board[x][y] == '':
            board[x][y] += last
            main.counter += 1
        else:
            print('taker'); main.counter -= 1
        status, winner, boxes = main.winCheck(board, winCombinations)
        if status or main.drawCheck(board) == True:
            main.winner = winner
            print(main.winner)
            main.boxes = boxes
            return main.counter, main.winner, main.boxes

    def Selfgame(self, board, winCombinations):
        gameStatus = True
        counter: int = 0
        last = 'x'
        while gameStatus:
            time.sleep(2)
            x: int = random.randint(0, 2)
            y: int = random.randint(0, 2)
            if board[x][y] == '':
                if counter % 2 == 0:
                    board[x][y] += 'x'
                    last: str = 'x'
                    counter += 1
                else:
                    board[x][y] += 'o'
                    last: str = 'o'
                    counter += 1
            else:
                pass

            if main.winCheck(board, winCombinations) == True:
                print('here')
                [print(i) for i in board]
                return 0
            if main.drawCheck(board):
                return 0

    def easyBot(self, board, winCombinations, playerSide):
        print("ZALUPA")
        gameStatus = True

        if playerSide == 'o':
            botSide = 'x'
        else:
            botSide = 'o'

        if playerSide == 'x':
            print('player choose - x')
        else:
            print('player choose - o');
            board[random.randint(0, 2)][random.randint(0, 2)] += 'x'
            [print(i) for i in board]
        while gameStatus:

            while empty == 0:
                x: int = random.randint(0, 2)
                y: int = random.randint(0, 2)
                if board[x][y] == '': board[x][y] += botSide; empty = 1; [print(i) for i in board]
                last = botSide

            if main.winCheck(board, winCombinations) == False or main.drawCheck(board) == True: [print(i) for i in
                                                                                                 board]; break

    def hardBot(self, board):

        gameStaus = True
        side: str = input('Chose your side', )
        print(f'U choosed "{side}" side')
        if side == 'o':
            sidebot = 'x'
            board[1][1] += 'x'
        else:
            sidebot = 'o'

        while gameStaus:
            x, y = map(int, input().split())
            if board[x][y] == '':
                board[x][y] = side
                empty = 0
                last = side
            else:
                print('Читы убрал')

            if main.winCheck(board, main.winCombinations) == False or main.drawCheck(board) == True: [print(i) for i in
                                                                                                      board]; break

            AI.AI(board, sidebot)

            if main.winCheck(board, main.winCombinations) == False or main.drawCheck(board) == True: [print(i) for
                                                                                                      i in
                                                                                                      board]; break
            [print(i) for i in board]

    def player_move(self, x, y, board, playerSide, winCombinations):
        if playerSide == 'o':
            botSide = 'x'
        else:
            botSide = 'o'
        if board[x][y] == '':
            board[x][y] = playerSide
            empty = 0
            last = playerSide
        else:
            print('pos has actualy taken')

        if main.winCheck(board, winCombinations) or main.drawCheck(board) == True:
            return 0
        while True:
            x: int = random.randint(0, 2)
            y: int = random.randint(0, 2)
            if board[x][y] == '': board[x][y] += botSide; empty = 1; [print(i) for i in board];break

        return 0

    def hard_player_move(self, x, y, board, playerSide, winCombinations):
        print('moved')
        if playerSide == 'x':
            sidebot = 'o'
        else:
            sidebot = 'x'
        if board[x][y] == '':
            board[x][y] = playerSide
        else:
            print('pos has actualy taken')
            return 0
        if main.winCheck(board, winCombinations) or main.drawCheck(board) == True:
            return 0
        AI.AI(board, sidebot)
        if main.winCheck(board, winCombinations) or main.drawCheck(board) == True:
            return 0
