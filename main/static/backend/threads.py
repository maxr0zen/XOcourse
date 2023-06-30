import multiprocessing
import gamemodes
import main

selfgame_thread = multiprocessing.Process(target=gamemodes.gamemodes.Selfgame, args=(gamemodes.gamemodes, main.board, main.winCombinations))
singlegame = multiprocessing.Process(target=gamemodes.gamemodes.singlePlay, args=(gamemodes.gamemodes, main.board, main.winCombinations))

def selfgame():
    flag = True
    if not selfgame_thread.is_alive() and flag == True:
        selfgame_thread.start()
        flag = False
    else: selfgame_thread.terminate()
