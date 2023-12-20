from dataclasses import dataclass
from typing import Type


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

def tiles_factory(tile: Type[Tile] = Tile,
                    width:int = 9, height:int = 9) -> list:
    return [[tile(x, y)
            for x in range(width)]
            for y in range(height)]
