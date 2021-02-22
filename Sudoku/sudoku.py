import argparse

import pandas as pd
import random
from tkinter import messagebox
import tkinter as tk
import sys







class Sudoku:
    """ Handles the data of the game """

    def __init__(self):
        self.puzzle = ''    # keep initial puzzle
        self.solution = ''  # keep solution
        self.current = ''   # keep current status with user choices
        self.new_game()

    def new_game(self):
        """ Selects a random game from the file """
        df = pd.read_csv('sudoku.csv')
        rand = random.randint(1, 1000000)

        self.puzzle = df['quizzes'][rand]
        self.current = df['quizzes'][rand]
        self.solution = df['solutions'][rand]



    def puzzle_value_at(self, row, col):
        return self.puzzle[row*9+col]

    def current_value_at(self, row, col):
        return self.current[row*9+col]

    def solution_value_at(self, row, col):
        return self.solution[row*9+col]

    def set_value_at(self, row, col, val):
        self.current = self.current[:row*9+col] + val + self.current[row*9+col+1:]

    def solved(self):
        return self.current == self.solution


class Cell:
    """ Represents one cell of the game with all its functionality """

    def __init__(self, frame, row, col, clicked):
        """
        Initializes the cell
        :param frame: The frame (block) where the cell will be placed
        :param row: the row in the whole sudoku board
        :param col: the column in the whole sudoku board
        :param clicked: Callback function to call when clicked
        """
        self.row = row
        self.col = col
        self.clicked = clicked
        self.label = tk.Label(master=frame, relief=tk.RAISED, borderwidth=1,
                              text=' ', height=2, width=4, font="Verdana 20 bold")
        self.label.grid(row=row % 3, column=col % 3, padx=1, pady=1)
        self.activate()

    def select(self):
        self.label['bg'] = "lightgray"

    def deselect(self):
        self.label['bg']= "white"

    def activate(self):
        self.label.bind("<Button-1>", lambda e: self.clicked(row=self.row, col=self.col))

    def deactivate(self):
        """ Used for cells that have a value given by the game and cannot be changed """
        self.label['bg'] = "white smoke"
        self.label.unbind("<Button-1>")

    def set_digit(self, ch):
        self.label['text'] = ch

    def set_wrong(self):
        self.label['fg'] = "red3"

    def set_correct(self):
        self.label['fg'] = "black"

    def clear(self):
        self.set_correct()
        self.label["text"] = ' '
        self.deselect()
        self.activate()


class Block:
    """ Represents a block of the game. A block is a 3x3 box """

    def __init__(self, window, row, col, cells, clicked):
        """
        Initializes the block
        :param window: window to be placed
        :param row: the row on the window
        :param col: the column on the window
        :param cells: A reference to the cells list in order to add the appropriate ones
        :param clicked: Callback function to be passed to the cells
        """
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=row, column=col, padx=1, pady=1)
        for r in range(3):
            for c in range(3):
                cell = Cell(frame, row*3+r, col*3+c, clicked)
                cells[row*3+r][col*3+c] = cell


class SudokuUI:
    """ Main frame of the application """

    def __init__(self):
        self.active = None
        self.game = Sudoku()
        self.window = tk.Tk()
        self.cells = [[None] * 9, [None] * 9, [None] * 9, [None] * 9, [None] * 9,
                      [None] * 9, [None] * 9, [None] * 9, [None] * 9]
        for row in range(3):
            for col in range(3):
                block = Block(self.window, row, col, self.cells,
                              self.cell_clicked)
        self.window.title("Sudoku")
        self.window.bind("<Key>", self.key_pressed)  # catch keyboard events
        self.init_cells()
        self.window.mainloop()

    def init_cells(self):
        """ Gives initial values to the board depending on what the current game has """
        for row in range(9):
            for col in range(9):
                value = self.game.puzzle_value_at(row, col)
                self.cells[row][col].clear()
                if value != '0':
                    self.cells[row][col].set_digit(value)
                    self.cells[row][col].deactivate()

    def cell_clicked(self, row, col):
        """
        Callback function for the cells. Called when a cell is clicked
        :param row: Row of the cell triggered the event
        :param col: Column of the cell triggered the event
        """
        cell = self.cells[row][col]

        if self.active == cell:
            self.active.deselect()
            self.active = None
        else:
            if self.active is not None:
                self.active.deselect()
            self.active = cell
            self.active.select()

    def key_pressed(self, event):
        """
        Key pressed event.
        Update selected cell (id any and if key was a digit)
        and check if puzzle is solved
        """
        ch = event.keysym
        if ch.isdigit():
            if self.active is not None:
                if ch == '0':
                    self.active.set_digit(' ')
                    return
                self.active.set_digit(ch)
                if ch == self.game.solution_value_at(self.active.row, self.active.col):
                    self.active.set_correct()
                else:
                    self.active.set_wrong()
                self.game.set_value_at(self.active.row, self.active.col, ch)
                if self.game.solved():
                    answer = messagebox.askquestion('SOLVED!', 'Play Again?')
                    if answer == 'yes':
                        self.game.new_game()
                        self.init_cells()
                        return
                    else:
                        self.window.destroy()
                        sys.exit()


if __name__ == '__main__':
    sudoku = SudokuUI()
