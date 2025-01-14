import random
import time

from cell import Cell


class Maze():
    WALL_PAIRS = {
            "left": ("has_left_wall", "has_right_wall"),
            "top": ("has_top_wall", "has_bottom_wall"),
            "right": ("has_right_wall", "has_left_wall"),
            "bottom": ("has_bottom_wall", "has_top_wall"),
    }

    DIRECTION_OFFSETS = {
        "left": (-1, 0),
        "top": (0, -1),
        "right": (1, 0),
        "bottom": (0, 1),
    }

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([ Cell(self._win) for i in range(self._num_rows)])

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = i * self._cell_size_x + self._x1
        x2 = x1 + self._cell_size_x
        y1 = j * self._cell_size_y + self._y1
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        i, j = 0, 0
        self._cells[i][j].has_top_wall = False
        self._draw_cell(i, j)

        i, j = self._num_cols - 1, self._num_rows - 1
        self._cells[i][j].has_bottom_wall = False
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            next_cells = []
            for direction, (di, dj) in self.DIRECTION_OFFSETS.items():
                next_i = i + di
                next_j = j + dj
                if next_i >= 0 and next_j >= 0 and next_i < self._num_cols and next_j < self._num_rows:
                    if not self._cells[next_i][next_j].visited:
                        next_cells.append((next_i, next_j, direction))

            if len(next_cells) == 0:
                self._draw_cell(i, j)
                return

            next_cell_col, next_cell_row, direction = next_cells[random.randrange(len(next_cells))]
            chosen_cell = self._cells[next_cell_col][next_cell_row]

            setattr(current_cell, self.WALL_PAIRS[direction][0], False)
            setattr(chosen_cell, self.WALL_PAIRS[direction][1], False)
            self._break_walls_r(next_cell_col, next_cell_row)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
