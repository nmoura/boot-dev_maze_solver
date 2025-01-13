from graphics import Line, Point


class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self._wall_color = "black"

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, self._wall_color)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, self._wall_color)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, self._wall_color)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, self._wall_color)

    def draw_move(self, to_cell, undo=False):
        source_x = (self._x1 + self._x2) // 2
        source_y = (self._y1 + self._y2) // 2
        destiny_x = (to_cell._x1 + to_cell._x2) //2
        destiny_y = (to_cell._y1 + to_cell._y2) //2

        line_color = "red"
        if undo:
            line_color = "gray"

        line = Line(Point(source_x, source_y), Point(destiny_x, destiny_y))
        self._win.draw_line(line, line_color)
