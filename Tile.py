from dataclasses import dataclass, field


def is_white(coordx:int, coordy:int) -> bool:
    if (coordx + coordy) % 2 == 0:
        return False
    return True

@dataclass(slots=True)
class Tile:
    coordx: int
    coordy: int
    white: bool = field(init=False)

    def __post_init__(self):
        self.white = is_white(self.coordx, self.coordy)
