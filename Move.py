from dataclasses import dataclass, field
from Tile import Tile


def is_atack(where: Tile) -> bool:
    pass

@dataclass
class Move:
    where: type(Tile)
    atack: bool = field(init=False)
    
    def __post_init__(self):
        self.atack = is_atack(self.where)
    