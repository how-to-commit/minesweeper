class Interface:
    def __init__(self, board):
        self.board = board
        self.end = False


    def updateDisplay(self):
        # prints <ESC> to clear screen
        # not portable, Windows only (I think)
        # replace with chr(27) + "[2J" to clear terminal on Unix systems, or ncurses.
        print('\033c', end='')
        self.showBoard()


    def promptCoordInput(self):
        # Python representation of REPEAT...UNTIL used to filter user input 
        while True:
            operation = input("Enter operation (f to flag or unflag a tile | r to reveal the tile): ")
            if operation in ('f', 'r'):
                break
            print("Invalid operation.")

        while True:
            col = input("Enter column number (numbers on top): ")
            if col.isnumeric():
                if (0 <= int(col) <= self.board.cols - 1):
                    col = int(col)
                    break
            print("Please enter only the numbers indicated at the top of the grid (starts with 0)!")
        
        while True:
            row = input("Enter row number (numbers on left): ")
            if row.isnumeric():
                if (0 <= int(row) <= self.board.rows - 1):
                    row = int(row)
                    break
            print("Please enter only the numbers indicated by the left of the grid (starts with 0)!")
        
        # calls setter functions here
        if operation == 'f':
            self.board.onflag(row, col)
        elif operation == 'r':
            self.board.onclick(row, col)
        
        self.updateDisplay()
        self.endGame(row, col)


    def start(self):
        print('\033c', end='')
        while True:
            rows = input("Enter number of rows: ")
            if rows.isnumeric():
                rows = int(rows)
                break
        while True:
            cols = input("Enter number of columns: ")
            if cols.isnumeric():
                cols = int(cols)
                break
        while True:
            mines = input("Enter number of mines: ")
            if mines.isnumeric():
                mines = int(mines)
                break
        self.board._setBoard(rows, cols, mines)


    def endGame(self, click_row, click_col):
        if self.board.winCheck():
            print("You won!")
            self.end = True
        elif self.board.loseCheck(click_row, click_col):
            print("You lost :(")
            self.end = True


    #========================================================#
    #                                                        #
    #             cancer starts here, bewarned               #
    #                                                        #
    #========================================================#
    def showBoard(self):
        """Unicode magick to box drawing characters"""
        # TODO: definitely make this nicer (changing used unicode characters into const?) later; i dont understand it either don't worry
        # is just abusing string concat with Unicode box-drawing chars
        # 0x2500, 0x2502, 0x2510, 0x250C, 0x2514, 0x2518, 0x251C, 0x2524, 0x2534, 0x253C, listed numerically for reference.
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