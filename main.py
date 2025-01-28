from window import Window
from geometry import Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 50), Point(750, 50)), "red")
    win.draw_line(Line(Point(50, 0), Point(50, 550)), "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()