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

class PiecesFactory(ABC):
    @abstractmethod
    def get_white_piece(self) -> Piece:
        pass

    @abstractmethod
    def get_black_piece(self) -> Piece:
        pass   

@dataclass
class Pawn(Piece):
    value: int = field(default=1, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class PawnFactory(PiecesFactory):
    def get_white_piece(self, tile:Tile) -> Piece:
        return Pawn(tile, True)

    def get_black_piece(self, tile:Tile) -> Piece:
        return Pawn(tile, False)
    
@dataclass
class Knight(Piece):
    value: int = field(default=3, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class KnightFactory(PiecesFactory):
    def get_white_piece(self, tile:Tile) -> Piece:
        return Knight(tile, True)

    def get_black_piece(self, tile:Tile) -> Piece:
        return Knight(tile, False)
    
@dataclass
class Bishop(Piece):
    value: int = field(default=3, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class BishopFactory(PiecesFactory):
    def get_white_piece(self, tile:Tile) -> Piece:
        return Bishop(tile, True)

    def get_black_piece(self, tile:Tile) -> Piece:
        return Bishop(tile, False)
    
@dataclass
class Rook(Piece):
    value: int = field(default=5, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class RookFactory(PiecesFactory):
    def get_white_piece(self, tile:Tile) -> Piece:
        return Rook(tile, True)

    def get_black_piece(self, tile:Tile) -> Piece:
        return Rook(tile, False)

@dataclass
class Queen(Piece):
    value: int = field(default=9, init=False, repr=False)

    def possible_movement(self) -> tuple:
        pass

class QueenFactory(PiecesFactory):
    def get_white_piece(self, tile:Tile) -> Piece:
        return Queen(tile, True)

    def get_black_piece(self, tile:Tile) -> Piece:
        return Queen(tile, False)
