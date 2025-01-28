class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point Object with co-ordinates x: {self.x}, y: {self.y}"

class Line:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill=fill_colour, width=2)

    def __repr__(self):
        return f"Line Object from {self.pointA} to {self.pointB}"

class Cell:
    def __init__(self, win = None, x1 = 0, y1 = 0, x2 = 0, y2 = 0, has_left_wall = True, has_top_wall = True, has_right_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win

    def draw(self):
        win = self.__win
        if self.has_left_wall:
            win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black")
        if self.has_top_wall:
            win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black")
        if self.has_right_wall:
            win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black")
        if self.has_bottom_wall:
            win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black")

    def draw_move(self, to_cell, undo = False):
        win = self.__win
        fill_colour = "red"
        if undo:
            fill_colour = "gray"
        win.draw_line(Line(Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2), Point((to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2)), fill_colour)

    def __repr__(self):
        return f"Cell Object from co-ordinates x: {self.__x1}, y: {self.__y1} to x: {self.__x2}, y: {self.__y2}"