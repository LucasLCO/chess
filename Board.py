from typing import Type, Union, Dict, List
from dataclasses import dataclass, field
from Piece import PieceFactory, Piece
from utils import color
from Tile import Tile
import json


def assemble_tiles(tile: Type[Tile]) -> list:
    return [[tile(x, y)
            for x in range(8)]
            for y in range(8)]

def load_pieces(path:str) -> dict:
    with open(path) as file:
        return json.load(file)

def matrix_to_string(matrix:list) -> str:
    formated_matrix = ""
    for row in matrix:
        formatted_row = " ".join(map(str, row))
        formated_matrix += formatted_row + "\n"

    return formated_matrix

PiecesDictionary = Dict[str, Union[Dict[str, List[Piece]],
                                    List[Piece]]]
def assemble_board(file_pieces: dict, tiles: list,
                    piece_factory: PieceFactory) -> PiecesDictionary:
    def iterate_file_pieces(color:str) -> None:
        pieces[color] = {}
        for piece_name in file_pieces["pieces"][color]:
            pieces[color][piece_name] = []
            for coords in file_pieces["pieces"][color][piece_name]:
                piece = piece_factory(piece_name,
                                    tiles[coords[1]][coords[0]], True)
                pieces[color][piece_name].append(piece)
                pieces["all"].append(piece)

    pieces: PiecesDictionary = {
                "all":[]
            }

    iterate_file_pieces("white")
    iterate_file_pieces("black")

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

    def get_white_piece(self,piece_color:str,  piece_name:str,
                        coordx, coordy) -> Union[Piece, None]:
        for piece in self._pieces[piece_color][piece_name]:
            if piece.tile.coordx == coordx \
            and piece.tile.coordy == coordy:

                return piece

        return None

    def __str__(self) -> str:
        INITIAL_NUMBER = 1
        SCENE_PADDING = 2
        SCENE_DIM = 10
        BOARD_DIM = 8

        board = [[" " for _ in range(SCENE_DIM)]
                    for __ in range(SCENE_DIM)]

        for i in range(BOARD_DIM):
            board[-1][-1-i] = chr(ord('h')-i)
            board[i][0] = i + INITIAL_NUMBER

        for row in self._tiles:
            for tile in row:
                board[tile.coordy][tile.coordx+SCENE_PADDING] = \
                f"{color.fg_lightgreen}.{color.reset}" if not tile.white \
                else f"{color.fg_green}{color.bg_black}.{color.reset}"

        for piece in self._pieces["all"]:
            board[piece.tile.coordy][piece.tile.coordx+SCENE_PADDING] = \
            f"{color.fg_lightgreen}{piece.name}{color.reset}" if not piece.white \
            else f"{color.fg_green}{color.bg_black}{piece.name}{color.reset}"

        return matrix_to_string(board)

@dataclass
class BoardFactory:
    tiles: list = field(init=False, repr=False)
    piece_factory: Type[PieceFactory] = field(init=False,
                                            repr=False,
                                            default_factory=PieceFactory)
    pieces: dict = field(init=False, repr=False)
    board_file_path: str = field(repr=False)

    def __post_init__(self) -> None:
        self.tiles = assemble_tiles(Tile)
        file_data = load_pieces(self.board_file_path)
        self.pieces = assemble_board(file_data, self.tiles, self.piece_factory)

    def __call__(self) -> Board:
        return Board(self.tiles, self.pieces)
