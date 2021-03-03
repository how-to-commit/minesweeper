from board import *
from interface import *
from time import sleep



_board = Board()
_interface = Interface(_board)

while True:
    _interface.start()
    _interface.updateDisplay()

    while True:
        _interface.promptCoordInput()
        sleep(1)
        if _interface.end:
            sleep(1)
            break
            