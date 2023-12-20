from dataclasses import dataclass, field
from pieces import PieceFactory, Piece
from typing import List, Union
from itertools import chain
from tile import Tile

@dataclass
class PieceGroup:
    color: str
    pawn: List[Piece] = field(default_factory=list, init=False)
    knight: List[Piece] = field(default_factory=list, init=False)
    bishop: List[Piece] = field(default_factory=list, init=False)
    rook: List[Piece] = field(default_factory=list, init=False)
    queen: List[Piece] = field(default_factory=list, init=False)
    king: List[Piece] = field(default_factory=list, init=False)

    @property
    def all(self) -> List[Piece]:
        return list(chain(self.pawn, self.knight, self.bishop,
                          self.rook, self.queen, self.king))

@dataclass
class Pieces:
    white = PieceGroup("white")
    black = PieceGroup("black")

    @property
    def all(self) -> List[Piece]:
        return self.white.all + self.black.all
    
    def match_tile_piece(self, tile: Tile) -> Union[Piece, None]:
        for piece in self.all:
            if piece.tile == tile:
                return piece

        return None


class PiecesFactory():
    def __init__(self, piece_file_data: dict,
                tiles: list, piece_factory: PieceFactory) -> None:
        self._piece_file_data = piece_file_data
        self._tiles = tiles
        self._piece_factory = piece_factory

    def __call__(self):
        pieces = Pieces()
        def iterate_file_pieces(piece_group:PieceGroup) -> Pieces:
            for piece_name in self._piece_file_data["pieces"][piece_group.color]:
                for coords in self._piece_file_data["pieces"][piece_group.color][piece_name]:
                    piece = self._piece_factory(piece_name,
                                        self._tiles[coords[1]][coords[0]],
                                        piece_group.color=="white")

                    vars(piece_group)[piece_name].append(piece)

        iterate_file_pieces(pieces.white)
        iterate_file_pieces(pieces.black)

        return pieces
