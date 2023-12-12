from abc import ABC, abstractmethod
from dataclasses import dataclass
from Tile import Tile


@dataclass
class Piece(ABC):
    tile: type(Tile)
    white: bool
    value: int

    @abstractmethod
    def possible_movement(self):
        pass