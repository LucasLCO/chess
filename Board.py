from Tile import Tile


class Board:
    def __init__(self) -> None:
        self._tiles = [[Tile(x, y)
                  for x in range(9)]
                  for y in range(9)]
        self._pieces = {"black":[],
                       "white":[]}

    @property
    def tiles(self):
        return [row[:] for row in self._tiles]

    def get_tile(self, coordx, coordy):
        return self._tiles[coordy][coordx]
