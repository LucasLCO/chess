from dataclasses import dataclass, field
from pieces import PieceFactory, Pieces ,PiecesFactory
from tile import Tile, tiles_factory
from typing import Type, Union
import json


class Color:
    RESET = '\033[0m'
    FG_LIGHTGREY = '\033[37m'
    FG_LIGHTGREEN = '\033[92m'
    FG_GREEN = '\033[32m'
    BG_BLACK = '\033[40m'

def load_pieces(path:str) -> dict:
    with open(path) as file:
        return json.load(file)

def matrix_to_string(matrix:list) -> str:
    formated_matrix = ""
    for row in matrix:
        formatted_row = " ".join(map(str, row))
        formated_matrix += formatted_row + "\n"

    return formated_matrix

class Board:
    def __init__(self, tiles: list, pieces: Pieces) -> None:
        self.tiles = tiles
        self.pieces = pieces

    def get_tile(self, coordx, coordy) -> Tile:
        return self.tiles[coordy][coordx]

    def __str__(self) -> str:
        INITIAL_NUMBER = 1
        CANVAS_PADDING = 2
        CANVAS_DIM = 10
        BOARD_DIM = 8

        board = [[" " for _ in range(CANVAS_DIM)]
                    for __ in range(CANVAS_DIM)]

        for i in range(BOARD_DIM):
            board[-1][-1-i] = chr(ord('h')-i)
            board[i][0] = i + INITIAL_NUMBER

        for row in self.tiles:
            for tile in row:
                board[tile.coordy][tile.coordx+CANVAS_PADDING] = \
                f"{Color.FG_LIGHTGREEN}.{Color.RESET}" if not tile.white \
                else f"{Color.FG_GREEN}{Color.BG_BLACK}.{Color.RESET}"

        for piece in self.pieces.all:
            board[piece.tile.coordy][piece.tile.coordx+CANVAS_PADDING] = \
            f"{Color.FG_LIGHTGREEN}{piece.name}{Color.RESET}" if not piece.white \
            else f"{Color.FG_GREEN}{Color.BG_BLACK}{piece.name}{Color.RESET}"

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
        self.tiles = tiles_factory()
        file_data = load_pieces(self.board_file_path)
        # self.pieces = assemble_board(file_data, self.tiles, self.piece_factory

    def __call__(self) -> Board:
        return Board(self.tiles, self.pieces)
