from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Nilton's Maze Solver")
        self.__canvas = Canvas(self.__root, bg="gray", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed")

    def draw_line(self, line, fill_color="blue"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="blue"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell():
    def __init__(self, p1, p2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self._win = win
        self._wall_color = "black"

    def draw(self):
        if self.has_left_wall:
            lw_p1 = Point(self._x1, self._y1)
            lw_p2 = Point(self._x1, self._y2)
            left_line = Line(lw_p1, lw_p2)
            self._win.draw_line(left_line, self._wall_color)
        if self.has_top_wall:
            tw_p1 = Point(self._x1, self._y1)
            tw_p2 = Point(self._x2, self._y1)
            top_line = Line(tw_p1, tw_p2)
            self._win.draw_line(top_line, self._wall_color)
        if self.has_right_wall:
            rw_p1 = Point(self._x2, self._y1)
            rw_p2 = Point(self._x2, self._y2)
            right_line = Line(rw_p1, rw_p2)
            self._win.draw_line(right_line, self._wall_color)
        if self.has_bottom_wall:
            bw_p1 = Point(self._x1, self._y2)
            bw_p2 = Point(self._x2, self._y2)
            bottom_line = Line(bw_p1, bw_p2)
            self._win.draw_line(bottom_line, self._wall_color)
