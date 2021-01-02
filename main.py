from board import *
from interface import *

_board = Board(rows=10, cols=10,mines=1)
_interface = Interface(_board)

_interface.updateDisplay()
while True:
    _interface.promptCoordInput()