from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Type
from tile import Tile


@dataclass
class Piece(ABC):
    name: str = field(repr=False)
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

@dataclass
class King(Piece):
    value: None = field(default=None,
                init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class PieceFactory:
    factories = {
        "pawn": (Pawn, "P"),
        "knight": (Knight, "N"),
        "bishop": (Bishop, "B"),
        "rook": (Rook, "R"),
        "queen": (Queen, "Q"),
        "king": (King, "K") 
    }

    def __call__(self, piece_type: str, tile: Tile,
                    is_white: bool) -> Piece:

        piece_class, piece_name = self.factories[piece_type]
        return piece_class(piece_name, tile, is_white)
