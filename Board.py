from dataclasses import dataclass, field
from Piece import PieceFactory, Piece
from typing import Type, Union
from Tile import Tile
import json

class fg:
    reset = '\033[0m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'


def tiles_factory(tile: Type[Tile]) -> list:
    return [[tile(x, y)
            for x in range(8)]
            for y in range(8)]

def load_pieces(path:str) -> dict:
    with open(path) as file:
        pieces = json.load(file)

    return pieces

def matrix_to_string(matrix:str) -> list:
    formated_matrix = ""
    for row in matrix:
        formatted_row = " ".join(map(str, row))
        formated_matrix += formatted_row + "\n"

    return formated_matrix

def asemble_board(file_pieces: dict, tiles: list, piece_factory: PieceFactory) -> dict:
    pieces = {}
    pieces["all"] = []
    pieces["white"] = {}
    for piece_name in file_pieces["pieces"]["white"]:
        pieces["white"][piece_name] = []
        for coords in file_pieces["pieces"]["white"][piece_name]:
            piece = piece_factory(piece_name, tiles[coords[1]][coords[0]], True)
            pieces["white"][piece_name].append(piece)
            pieces["all"].append(piece)


    pieces["black"] = {}
    for piece_name in file_pieces["pieces"]["black"]:
        pieces["black"][piece_name] = []
        for coords in file_pieces["pieces"]["black"][piece_name]:
            piece = piece_factory(piece_name, tiles[coords[1]][coords[0]], False)
            pieces["black"][piece_name].append(piece)
            pieces["all"].append(piece)

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

    def get_white_piece(self, piece_name:str, coordx, coordy) -> Union[Piece, None]:
        for piece in self._pieces["white"][piece_name]:
            if piece.tile.coordx == coordx and piece.tile.coordy == coordy:
                return piece

        return None

    def get_black_piece(self, piece_name:str, coordx, coordy) -> Union[Piece, None]:
        for piece in self._pieces["black"][piece_name]:
            if piece.tile.coordx == coordx and piece.tile.coordy == coordy:
                return piece

        return None

    def __str__(self) -> str:
        board = [[" " for x in range(10)]
                    for y in range(10)]

        for i in range(8):
            board[9][9-i] = chr(ord('h')-i)
            board[i][0] = i+1

        for row in self._tiles:
            for tile in row:
                board[tile.coordy][tile.coordx+2] = \
                f"{fg.lightgreen}.{fg.reset}" if not tile.white \
                else f"{fg.green}{bg.black}.{fg.reset}"

        for piece in self._pieces["all"]:
            board[piece.tile.coordy][piece.tile.coordx+2] = \
            f"{fg.lightgreen}{piece.name}{fg.reset}" if not piece.white \
            else f"{fg.green}{bg.black}{piece.name}{fg.reset}"

        return matrix_to_string(board)

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
