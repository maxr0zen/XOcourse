from django.shortcuts import render
import multiprocessing
import threading
import time
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from main.static.backend import gamemodes, main

thread = threading.Thread(target=gamemodes.modes.Selfgame, args=(gamemodes.modes, main.board, main.winCombinations))






def update(request):
    table = {
        'data00': main.board[0][0],
        'data01': main.board[0][1],
        'data02': main.board[0][2],
        'data10': main.board[1][0],
        'data11': main.board[1][1],
        'data12': main.board[1][2],
        'data20': main.board[2][0],
        'data21': main.board[2][1],
        'data22': main.board[2][2],
    }
    data = {'table': table}
    return HttpResponse(json.dumps(data), content_type='application/json')


def index(request):
    '''
    if thread.is_alive() == False:
        thread.start()
    '''
    return render(request, 'main/base.html')

def single(request):
    main.board = [['', '', ''],
                  ['', '', ''],
                  ['', '', '']]
    main.clear(board=main.board)

    return HttpResponse('пыска')

@csrf_exempt
def singleMove(request):
    if request.method == "POST":
        id_dict = json.loads(request.body)  # "0 0"
        id = id_dict['id']
        x,y = map(int, id.split(' '))
        singlegame = threading.Thread(target=gamemodes.modes.singlePlay,
                                      args=(gamemodes.modes, main.board, main.winCombinations, x, y, main.counter))
        print(main.board)
        if not main.winCheck(main.board, main.winCombinations) or not main.drawCheck(main.board):
            print('-')
            singlegame.start()
            #gamemodes.modes.singlePlay(gamemodes.modes, main.board, main.winCombinations, x, y, main.counter)
        winner = main.winner
        boxes = main.boxes
        return HttpResponse(json.dumps(winner), content_type='application/json')
    return HttpResponse('Piska 2')

def ezbot(request):
    return 0


@csrf_exempt
def choose_ezbot_side(request):
    player_side = json.loads(request.body)
    print(player_side["side"])

    if request.method == "POST":
        if player_side["side"] == 'o':
            easy = threading.Thread(target=gamemodes.modes.easyBot,
                                          args=(gamemodes.modes, main.board, main.winCombinations, player_side["side"]))
            easy.start()
    return HttpResponse('Piska 3')


@csrf_exempt
def choose_hardbot_side(request):
    player_side = json.loads(request.body)
    print(player_side["side"], "hard")
    if player_side["side"] == 'o':
        main.board[1][1] += 'x'

    return HttpResponse('Piska 3')


@csrf_exempt
def hard_move(request):
    if main.winCheck(main.board, main.winCombinations) or  main.drawCheck(main.board):
        return render(request, "main/index.html")
    else:
        player_side = json.loads(request.body)
        print(player_side['side'])
        if request.method == "POST":
            x, y = map(int, player_side["move"].split())
            print(x, y)
            hard = threading.Thread(target= gamemodes.modes.hard_player_move,
                                    args=(main.gamemodes,x,y,main.board,player_side["side"],main.winCombinations))
            if not main.winCheck(main.board, main.winCombinations) or not main.drawCheck(main.board):
                print('-')
                hard.start()

    return HttpResponse('Piska 3')


@csrf_exempt
def easy_move(request):
    if main.winCheck(main.board, main.winCombinations) or  main.drawCheck(main.board):
        return HttpResponse('1')
    else:
        player_side = json.loads(request.body)
        if request.method == "POST":
            x,y = map(int, player_side["move"].split())
            print(x,y)
            ez = threading.Thread(target=gamemodes.modes.player_move,
                                          args=(gamemodes.modes,x,y,main.board,player_side["side"],main.winCombinations))
            if not main.winCheck(main.board, main.winCombinations) or not main.drawCheck(main.board):
                print('-')
                ez.start()

    return HttpResponse('Piska 3')

def motion(request):
    return 0

