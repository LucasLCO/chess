from abc import ABC, abstractmethod
from dataclasses import dataclass
from ..Tile import Tile


@dataclass
class Piece(ABC):
    tile: Tile
    color: str

    @abstractmethod
    def possible_movement(self) -> tuple:
        pass

def move(piece: Piece, tile_to: Tile) -> None:
    piece.tile = tile_to
