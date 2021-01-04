import random



class Cell():
    def __init__(self, is_mine=False, is_vis=False, is_flag=False):
        # cell properties
        self.is_mine = is_mine
        self.is_vis = is_vis
        self.is_flag = is_flag
        self.number = 0


    # setter methods below
    def placeMine(self):
        self.is_mine = True


    def show(self):
        self.is_vis = True


    def flag(self):
        self.is_flag = not self.is_flag


    def incrementNum(self):
        """Increments displayed number (of bombs around cell) on cell.
        # WARN: DO NOT CALL THIS MID-GAME!"""
        self.number += 1



class Board():
    def _setBoard(self, rows=5, cols=5, mines=5):
        """setBoard sets up the board.
        WARN: DO NOT CALL THIS MID-GAME!"""
        
        self.rows = rows
        self.cols = cols
        self.mines = mines

        self.board = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]

        # setting mines
        for num_mines in range(self.mines):
            while True:
                randcol = random.randint(0, self.cols-1)
                randrow = random.randint(0, self.rows-1)
                if not self.board[randrow][randcol].is_mine:
                    break
            self.board[randrow][randcol].placeMine()

            # update cell numbers... 
            for dx in range(-1, 1+1):
                for dy in range(-1, 1+1):
                    if (0 <= randrow+dy <= self.rows-1) and (0 <= randcol+dx <= self.cols-1):
                        self.board[randrow+dy][randcol+dx].incrementNum()


    def winCheck(self):
        flagged_mine_count = 0
        vis_count = 0
        wincond_vis_count = self.rows * self.cols

        # counts flagged mines and visible numbers, you need all of them to win the game
        for row in self.board:
            for cell in row:
                if cell.is_mine and cell.is_flag:
                    flagged_mine_count += 1
                    vis_count += 1
                elif cell.is_vis:
                    vis_count += 1
        
        # checks wincond
        if (flagged_mine_count == self.mines) and (vis_count == wincond_vis_count):
            return True
        else:
            return False


    def loseCheck(self, click_row, click_col):
        # only loss condition is if you click on a mine
        # worked around by using click_row + click_col passed to it from interface.py
        if self.board[click_row][click_col].is_mine:
            return True
        else:
            return False


    def _dbg_ShowBoard(self):
        """Debug function to show all."""
        for vertx in self.board:
            for cell in vertx:
                cell.show()


    def onflag(self, row, col):
        self.board[row][col].flag()
    
    def onclick(self, row, col):
        self.onclick_empty = []

        # if clicked on number ONLY show number
        if (self.board[row][col].number > 0):
            self.board[row][col].show()

        # if clicked on blank show all connected blanks and adj numbers
        else: 
            for dcol in range(-1, 1+1):
                for drow in range(-1, 1+1):
                    # filter before sorting
                    if (0 <= col+dcol <= self.cols-1) and (0 <= row+drow <= self.rows-1) and not (self.board[row+drow][col+dcol].is_vis):

                        # all blanks
                        if not (self.board[row+drow][col+dcol].number > 0):
                            self.board[row+drow][col+dcol].show()
                            self.onclick_empty.append([row+drow, col+dcol])

                        # all nonblank numbers
                        else:
                            self.board[row+drow][col+dcol].show()

            # recurse here to get to the rest of the board
            # might need to finetune what gets handed to the list because its SLOW
            for _row, _col in self.onclick_empty:
                self.onclick(_row, _col)





