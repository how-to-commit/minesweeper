class Interface:
    def __init__(self, board):
        self.board = board


    def updateDisplay(self):
        # prints <ESC> to clear screen
        print('\033c', end='')
        self.showBoard()


    def promptCoordInput(self):
        while True:
            operation = input("Enter operation (f to flag or unflag a tile | r to reveal the tile): ")
            if operation in ('f', 'r'):
                break
            # error clause
            print("Invalid operation.")

        while True:
            col = input("Enter column number (numbers on top): ")
            if col.isnumeric():
                if (0 <= int(col) <= self.board.cols - 1):
                    col = int(col)
                    break
            # error clause:
            print("Please enter only the numbers indicated at the top of the grid (starts with 0)!")
        
        while True:
            row = input("Enter row number (numbers on left): ")
            if row.isnumeric():
                if (0 <= int(row) <= self.board.rows - 1):
                    row = int(row)
                    break
            # error clause:
            print("Please enter only the numbers indicated by the left of the grid (starts with 0)!")
        
        if operation == 'f':
            self.board.onflag(row, col)
        elif operation == 'r':
            self.board.onclick(row, col)
        
        self.updateDisplay()


    #========================================================#
    #             cancer starts here, bewarned               #
    #========================================================#
    def showBoard(self):
        """Unicode magick to box drawing characters"""
        # TODO: definitely make this nicer later; i dont understand it either don't worry
        loopct = 0
        print('   ', end='')

        for index in range(self.board.cols):
            print(" {}  ".format(index), end='')

        print('\n', end='')
        print("  " + u'\u250C' + (((u'\u2500' * 3) + u'\u252C') * self.board.cols) + '\b' + u'\u2510')

        for vertx in self.board.board:
            print(str(loopct) + ' ', end='')
            loopct += 1

            for cell in vertx:
                print(u'\u2502', end='')

                if cell.is_flag:
                    print(" F ", end='')

                elif cell.is_vis:
                    if cell.is_mine:
                        print(" M ", end='')
                    elif cell.number == 0:
                        print("   ", end='')
                    else:
                        print(" " + str(cell.number) + " ", end='')
                        
                else:
                    print(' ' + u'\u2588' + ' ', end='')

            print(u'\u2502')
            if not (vertx == self.board.board[-1]):
                print("  " + u'\u251C' + (((u'\u2500' * 3) + u'\u253C') * self.board.cols) + '\b' + u'\u2524')
        
        print("  " + u'\u2514' + (((u'\u2500' * 3) + u'\u2534') * self.board.cols) + '\b' + u'\u2518')