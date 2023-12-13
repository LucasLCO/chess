from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from Tile import Tile
from Move import Move


@dataclass
class Piece(ABC):
    tile: type(Tile)
    white: bool
    value: int = field(init=False)

    @abstractmethod
    def possible_movement(self) -> tuple:
        pass

@dataclass
class Pawn(Piece):
    value: int = field(default=1, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

