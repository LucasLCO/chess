from dataclasses import dataclass, field


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


class TilesFactory():
    pass