class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill=fill_colour, width=2)