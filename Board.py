from dataclasses import dataclass, field
from Piece import PieceFactory, Piece
from typing import Type, Union
from Tile import Tile
import json

# TODO
# See if the factory pattern is really
# the solution here and how to improve
# the pieces_locationd function and implement
# the get piece on Board function

def tiles_factory(tile: Type[Tile]) -> list:
    return [[tile(x, y)
            for x in range(8)]
            for y in range(8)]

def load_pieces(path:str) -> dict:
    with open(path) as file:
        pieces = json.load(file)

    return pieces

def asemble_board(file_pieces: dict, tiles: list, piece_factory: PieceFactory) -> dict:
    pieces : dict[str, dict[str, list]] = {}
    pieces["white"] = {}
    for piece_name in file_pieces["pieces"]["white"]:
        pieces["white"][piece_name] = []
        for coords in file_pieces["pieces"]["white"][piece_name]:
            pieces["white"][piece_name].append(
                piece_factory(piece_name, tiles[coords[1]][coords[0]], True)
            )

    pieces["black"] = {}
    for piece_name in file_pieces["pieces"]["black"]:
        pieces["black"][piece_name] = []
        for coords in file_pieces["pieces"]["black"][piece_name]:
            pieces["black"][piece_name].append(
                piece_factory(piece_name, tiles[coords[1]][coords[0]], False)
            )

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

    def get_piece(self, white:bool, piece_name:str, coordx, coordy) -> Piece:
        for piece in self._pieces["white" if white else "black"][piece_name]:
            if piece.tile.coordx == coordx and piece.tile.coordy == coordy:
                return piece

        return None

@dataclass
class BoardFactory:
    tiles: list = field(init=False, repr=False)
    piece_factory: Type[PieceFactory] = field(init=False, repr=False, default_factory=PieceFactory)
    pieces: dict = field(init=False, repr=False)
    board_file_path: str = field(repr=False)

    def __post_init__(self) -> None:
        self.tiles = tiles_factory(Tile)
        file_data = load_pieces(self.board_file_path)
        self.pieces = asemble_board(file_data, self.tiles, self.piece_factory)

    def __call__(self) -> Board:
        return Board(self.tiles, self.pieces)
