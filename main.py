from window import Window
from geometry import Point, Line, Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(True, True, True, True, 50, 50, 100, 100, win)
    cell1.draw()
    cell2 = Cell(True, True, True, True, 110, 50, 160, 100, win)
    cell2.draw()
    cell1.draw_move(cell2)
    win.wait_for_close()


if __name__ == "__main__":
    main()