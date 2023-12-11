from dataclasses import dataclass
import string

def gen_color(coord) -> str:
    if (ord(coord[0]) + int(coord[1])) % 2 == 0:
        return 'b'
    return 'w'


@dataclass(slots=True, frozen=True)
class Tile:
    coord : str
    color : str
    
    @classmethod
    def from_coord(cls, coord: str) -> "Tile":
        color = gen_color(coord)
        return cls(coord, color)

coords = [[Tile.from_coord(f"{letter}{number}").color for letter in list(string.ascii_letters)[:8]] for number in range(8,0,-1)]

for row in coords:
    print(row)
        

