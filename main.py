from window import Window
from geometry import Point, Line, Cell
from maze import Maze

def main():
    win = Window(1920, 1080)
    maze = Maze(50, 50, 20, 20, 50, 50, win)
    maze._solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()