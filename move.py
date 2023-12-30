from dataclasses import dataclass
from tile import Tile, Tiles
from enum import Enum, auto
from pieces import Piece


def pawn(tile: Tile, tiles: Tiles) -> list:
    return [tiles.get_tile(tile.coordx, tile.coordy+1),
            tiles.get_tile(tile.coordx+1, tile.coordy+1),
            tiles.get_tile(tile.coordx-1, tile.coordy+1)]

def knight(tile: Tile, tiles: Tiles) -> list:
    pass

def bishop(tile: Tile, tiles: Tiles) -> list:
    pass

def rook(tile: Tile, tiles: Tiles) -> list:
    pass

def queen(tile: Tile, tiles: Tiles) -> list:
    pass

def king(tile: Tile, tiles: Tiles) -> list:
    pass

class MoveState(Enum):
    POSSIBLE = auto()
    ATACK = auto()

class MoveHandler:
    piece_dict = {
        "P": pawn
    }
    
    def __init__(self, tiles: Tiles) -> None:
        self.tiles = tiles

    def __call__(self, piece: Piece, tile_to: Tile) -> bool:   
        possible_tiles = self.piece_dict[piece.name](piece.tile, self.tiles)
        if tile_to in possible_tiles:
            piece.tile = tile_to
            return True
        return False

