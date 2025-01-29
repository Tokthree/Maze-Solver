from time import sleep
from geometry import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.__num_cols):
            self._cells.append([])
            for j in range(self.__num_rows):
                current_cell_x1 = self.__x1 + (self.__cell_size_x * i)
                current_cell_x2 = current_cell_x1 + self.__cell_size_x
                current_cell_y1 = self.__y1 + (self.__cell_size_y * j)
                current_cell_y2 = current_cell_y1 + self.__cell_size_y
                self._cells[i].append(Cell(self.__win, current_cell_x1, current_cell_y1, current_cell_x2, current_cell_y2))

        if self.__win is not None:     
            for i in range(self.__num_cols):
                for j in range(self.__num_rows):
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.__win.redraw()
        sleep(0.05)