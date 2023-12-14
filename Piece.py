from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Type
from Tile import Tile


@dataclass
class Piece(ABC):
    tile: Type[Tile]
    white: bool
    value: int = field(init=False)

    @abstractmethod
    def possible_movement(self) -> tuple:
        pass

@dataclass
class Pawn(Piece):
    value: int = field(default=1,
                init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Knight(Piece):
    value: int = field(default=3,
                init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Bishop(Piece):
    value: int = field(default=3,
                init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Rook(Piece):
    value: int = field(default=5,
                init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Queen(Piece):
    value: int = field(default=9,
                init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class PieceFactory:
    factories = {
        "pawn": Pawn,
        "knight": Knight,
        "bishop": Bishop,
        "rook": Rook,
        "queen": Queen,
    }

    def __call__(self, piece_type: str, tile: Tile,
                    is_white: bool) -> Piece:

        piece_class = self.factories[piece_type]
        return piece_class(tile, is_white)
