from board import *
from interface import *

_board = Board()
_interface = Interface(_board)

while True:
    _interface.start()
    _interface.updateDisplay()

    while True:
        _interface.promptCoordInput()
        if _interface.end:
            break