from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Protocol, Type
from Tile import Tile
from Move import Move


# Make an named tuple to create the 
# instaces of the pices to not have 
# to import all pieces types, just
# the factory to create the pieces 

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
    value: int = field(default=1, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Knight(Piece):
    value: int = field(default=3, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Bishop(Piece):
    value: int = field(default=3, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Rook(Piece):
    value: int = field(default=5, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

@dataclass
class Queen(Piece):
    value: int = field(default=9, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class PieceFactory:
    def get_piece(self, piece_type: Type[Piece],
                tile: Tile, is_white: bool) -> Piece:

        return piece_type(tile, is_white)