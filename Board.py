from dataclasses import dataclass, field
from Piece import PieceFactory
from typing import Type
from Tile import Tile
# , tiles, pieces
# The tiles and picies should not be
# a responsability to Board create.
# make an BoardBuilder and pass tiles
# and picies as reference on the __init__

        # self._tiles = [[Tile(x, y)
        #           for x in range(9)]
        #           for y in range(9)]
        # self._pieces = {"black":[],
        #                "white":[]}

def tiles_factory(tile: Type[Tile]):
    return [[tile(x, y)
            for x in range(9)]
            for y in range(9)]

class Board:
    def __init__(self, tiles: list, pieces: dict) -> None:
        self._tiles = tiles
        self._pieces = pieces

    @property
    def tiles(self):
        return [row[:] for row in self._tiles]

    def get_tile(self, coordx, coordy):
        return self._tiles[coordy][coordx]

@dataclass
class BoardFactory:
    tiles: list = field(init=False, repr=False)
    piece_factory: Type[PieceFactory] = field(init=False, repr=False,
                                            default_factory=PieceFactory)

    def __post_init__(self):
        self.tiles = tiles_factory(Tile)

    def __call__(self):
        pass
