from pieces import PieceFactory, Pieces, PiecesFactory
from dataclasses import dataclass
from tile import Tiles
import json


def load_board(path:str) -> dict:
    with open(path) as file:
        return json.load(file)

def matrix_to_string(matrix:list) -> str:
    formated_matrix = ""
    for row in matrix:
        formatted_row = " ".join(map(str, row))
        formated_matrix += formatted_row + "\n"

    return formated_matrix

class Color:
    RESET = '\033[0m'
    FG_LIGHTGREY = '\033[37m'
    FG_LIGHTGREEN = '\033[92m'
    FG_GREEN = '\033[32m'
    BG_BLACK = '\033[40m'

class CanvasConfig:
    INITIAL_NUMBER = 1
    CANVAS_PADDING = 2
    CANVAS_DIM = 10
    BOARD_DIM = 8

@dataclass
class Board:
    tiles: Tiles
    pieces: Pieces

class BoardRenderer:
    def __init__(self, board: Board) -> None:
        self.board = board

    def __str__(self) -> str:
        board = [[" " for _ in range(CanvasConfig.CANVAS_DIM)]
                    for __ in range(CanvasConfig.CANVAS_DIM)]

        for i in range(CanvasConfig.BOARD_DIM):
            board[-1][-1-i] = chr(ord('h')-i)
            board[i][0] = i + CanvasConfig.INITIAL_NUMBER

        for tile in self.board.tiles.all:
            board[tile.coordy][tile.coordx+CanvasConfig.CANVAS_PADDING] = \
            f"{Color.FG_LIGHTGREEN}.{Color.RESET}" if tile.white \
            else f"{Color.FG_GREEN}{Color.BG_BLACK}.{Color.RESET}"

        for piece in self.board.pieces.all:
            board[piece.tile.coordy][piece.tile.coordx+CanvasConfig.CANVAS_PADDING] = \
            f"{Color.FG_LIGHTGREEN}{piece.name}{Color.RESET}" if piece.white \
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

    def create_board(self) -> Board:
        return Board(self._tiles, self._pieces)

    def create_board_renderer(self, board: Board) -> BoardRenderer:
        return BoardRenderer(board)
