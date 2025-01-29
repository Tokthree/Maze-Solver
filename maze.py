from time import sleep
import random
from geometry import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = None
        if seed is not None:
            self.__seed = random.seed(seed)
        self._create_cells()

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.__win.redraw()
        sleep(0.05)
    
    def _reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j].visited = False

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

            self._break_walls_r(0, 0)
            self._reset_cells_visited()
            self._break_entrance_and_exit()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            possible_directions = []

            if i != 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if i != len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j != 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if j != len(self._cells[i]) - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            else:
                random_direction = possible_directions[random.randrange(0, len(possible_directions))]
                random_i = random_direction[0]
                random_j = random_direction[1]

                if i > random_i:
                    self._cells[i][j].has_left_wall = False
                    self._cells[random_i][random_j].has_right_wall = False
                elif i < random_i:
                    self._cells[i][j].has_right_wall = False
                    self._cells[random_i][random_j].has_left_wall = False
                elif j > random_j:
                    self._cells[i][j].has_top_wall = False
                    self._cells[random_i][random_j].has_bottom_wall = False
                else:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[random_i][random_j].has_top_wall = False
                self._break_walls_r(random_direction[0], random_direction[1])