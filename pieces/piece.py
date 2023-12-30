from dataclasses import dataclass, field
from tile import Tile


@dataclass
class Piece:
    name: str = field(repr=False)
    tile: Tile
    white: bool
    value: int = field(init=False)

@dataclass
class Pawn(Piece):
    value: int = field(default=1,
                init=False, repr=False)

@dataclass
class Knight(Piece):
    value: int = field(default=3,
                init=False, repr=False)

@dataclass
class Bishop(Piece):
    value: int = field(default=3,
                init=False, repr=False)

@dataclass
class Rook(Piece):
    value: int = field(default=5,
                init=False, repr=False)

@dataclass
class Queen(Piece):
    value: int = field(default=9,
                init=False, repr=False)

@dataclass
class King(Piece):
    value: None = field(default=None,
                init=False, repr=False)

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
