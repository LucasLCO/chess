from dataclasses import dataclass, field
from Piece import PieceFactory, Piece
from typing import Type
from Tile import Tile


def tiles_factory(tile: Type[Tile]) -> list:
    return [[tile(x, y)
            for x in range(9)]
            for y in range(9)]

def pieces_position(tiles: list, piece_factory: PieceFactory) -> dict:
    pieces = {"white": [],
              "black": []}
    
    pieces_ord_list = ["rook", "knight", "bishop", "queen",
                    "king", "bishop", "knight", "rook"]

    for wp_tile, bp_tile, piece in zip(tiles[0], tiles[8], pieces_ord_list):
        pieces["white"].append(piece_factory(piece_type=piece,
                                            tile=wp_tile, is_white=True))
        pieces["black"].append(piece_factory(piece_type=piece,
                                            tile=bp_tile, is_white=False))

    for wp_tile, bp_tile in zip(tiles[1], tiles[7]):
        pieces["white"].append(piece_factory(piece_type='pawn',
                                            tile=wp_tile, is_white=True))
        pieces["black"].append(piece_factory(piece_type='pawn',
                                            tile=bp_tile, is_white=False))

    return pieces

class Board:
    def __init__(self, tiles: list, pieces: dict) -> None:
        self._tiles = tiles
        self._pieces = pieces

    @property
    def tiles(self) -> list:
        return [row[:] for row in self._tiles]

    def get_tile(self, coordx, coordy) -> Tile:
        return self._tiles[coordy][coordx]

    @property    
    def pieces(self):
        return self._pieces.copy()
    
    # def get_piece(self, tile_on: Tile, white:bool) -> Piece:
    #     if white:
    #         for piece in self._pieces['white']:
    #             if piece.tile == tile_on else None
            
@dataclass
class BoardFactory:
    tiles: list = field(init=False, repr=False)
    piece_factory: Type[PieceFactory] = field(init=False, repr=False, default_factory=PieceFactory)
    pieces: dict = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.tiles = tiles_factory(Tile)
        self.pieces = pieces_position(self.tiles, self.piece_factory)

    def __call__(self) -> Board:
        return Board(self.tiles, self.pieces)
