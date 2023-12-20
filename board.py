from dataclasses import dataclass, field
from pieces import PieceFactory, Pieces, PiecesFactory
from typing import Type
from tile import Tiles
import json


class Color:
    RESET = '\033[0m'
    FG_LIGHTGREY = '\033[37m'
    FG_LIGHTGREEN = '\033[92m'
    FG_GREEN = '\033[32m'
    BG_BLACK = '\033[40m'

def load_board(path:str) -> dict:
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

        for tile in self.tiles.all:
            board[tile.coordy][tile.coordx+CANVAS_PADDING] = \
            f"{Color.FG_LIGHTGREEN}.{Color.RESET}" if not tile.white \
            else f"{Color.FG_GREEN}{Color.BG_BLACK}.{Color.RESET}"

        for piece in self.pieces.all:
            board[piece.tile.coordy][piece.tile.coordx+CANVAS_PADDING] = \
            f"{Color.FG_LIGHTGREEN}{piece.name}{Color.RESET}" if not piece.white \
            else f"{Color.FG_GREEN}{Color.BG_BLACK}{piece.name}{Color.RESET}"

        return matrix_to_string(board)

class BoardFactory:
    def __init__(self, board_file_path) -> None:
        self._file_data = load_board(board_file_path)
        self._tiles = Tiles()
        self._piece_factory = PieceFactory()
        self._pieces_factory = PiecesFactory(self._file_data,
                                            self._tiles,
                                            self._piece_factory)
        self._pieces = self._pieces_factory()

    def __call__(self) -> Board:
        return Board(self._tiles, self._pieces)