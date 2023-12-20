from dataclasses import dataclass, field
from typing import List


def is_white(coordx:int, coordy:int) -> bool:
    if (coordx + coordy) % 2 == 0:
        return False
    return True

@dataclass(slots=True)
class Tile:
    coordx: int
    coordy: int

    @property
    def white(self) -> bool:
        return is_white(self.coordx, self.coordy)

def tile_board_factory(width:int, height:int) -> List[List[Tile]]:
    return [[Tile(x, y)
            for x in range(width)]
            for y in range(height)]

@dataclass
class Tiles:
    width: int = field(default=8)
    height: int = field(default=8)

    @property
    def tiles(self):
        return tile_board_factory(self.width, self.height)

    @property
    def all(self) -> List[Tile]:
        return [tile for row in self.tiles for tile in row]

    def get_tile(self, coordx:int, coordy:int) -> Tile:
        return self.tiles[coordy][coordx]

    def get_tiles_with_pieces(self, pieces:list) -> List[Tile]:
        tiles_pieces = []
        for piece in pieces:
            tiles_pieces.append(piece.tile)

        return tiles_pieces
    
    def get_empty_tiles(self, pieces:list) -> List[Tile]:
        tiles_pieces = self.tiles_with_pieces(pieces)
    
        return [tile for tile in self.all if tile not in tiles_pieces]
