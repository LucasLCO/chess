from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Type
from tile import Tile

# Instead of each piece to have
# the move described inside their
# own class, maybe the Move class
# should have implemented the specifics
# move calculators.

class MoveState(Enum):
    POSSIBLE = auto()
    NOT_POSSIBLE = auto()

def is_atack(where: Tile) -> bool:
    pass

@dataclass
class Move:
    where: Type[Tile]
    state: Type[MoveState]
    atack: bool = field(init=False)
    
    def __post_init__(self):
        self.atack = is_atack(self.where)
    
# Use enums to change the state of the tiles