from typing import List
from random import randint


class Cell:
    """
    Class of cell in the Gamepol object
    """
    around_mines: int
    mine: bool
    fl_open: bool = False  # Change on True for debug correct creating of table

    def __init__(self, around_mines: int, mine: bool) -> None:
        """
        Initialize cell of minesweeper's field,
        takes count of mines around and boolean value
        whether the cell is a mine
        """
        self.around_mines = around_mines
        self.mine = mine


class GamePole:
    side: int
    mines_count: int
    pole: List[List[Cell]]

    def __init__(self, side: int, mines_count: int) -> None:
        """
        Initialize object for control minesweeper's field,
        takes side of field and count of mines
        """
        self.side = side
        self.mines_count = mines_count
        self.pole = [[Cell(0, False) for _ in range(side)] for _ in range(side)]
        self.init()

    def init(self) -> None:
        """
        Create new field for minesweeper
        """
        mines_coords = self.get_random_mines_coord()
        for x, y in mines_coords:
            self.pole[x][y].mine = True
            around = (
                (x + 1, y), (x + 1, y - 1), (x + 1, y + 1),
                (x - 1, y), (x - 1, y - 1), (x - 1, y + 1), 
                (x, y - 1), (x, y + 1)
            )
            for x_around, y_around in around:
                if 0 <= x_around < self.side and 0 <= y_around < self.side:
                    self.pole[x_around][y_around].around_mines += 1

    def get_random_mines_coord(self) -> set:
        """
        Generate set of random mines coordinates 
        """
        mines_coords = set()
        while len(mines_coords) < self.mines_count:
            mines_coords.add((randint(0, self.side - 1), randint(0, self.side - 1)))
        return mines_coords

    def show(self) -> None:
        """
        Show current field of minesweeper
        """
        for row in self.pole:
            for cell in row:
                if cell.fl_open:
                    if cell.mine:
                        print("*", end=" ")
                    else:
                        print(cell.around_mines, end=" ")
                else:
                    print("#", end=" ")
            print()


pole_game = GamePole(10, 12)
