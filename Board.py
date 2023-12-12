from Tile import Tile


class Board:
    def __init__(self) -> None:
        self.tiles = [[Tile(x, y)
                  for x in range(9)]
                  for y in range(9)]
        self.pieces = None
