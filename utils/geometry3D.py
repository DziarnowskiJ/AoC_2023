from enum import Enum
from typing import Self


# compass points
class Direction(Enum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7

    U = 8
    NU = 9
    NEU = 10
    EU = 11
    SEU = 12
    SU = 13
    SWU = 14
    WU = 15
    NWU = 16

    D = 17
    ND = 18
    NED = 19
    ED = 20
    SED = 21
    SD = 22
    SWD = 23
    WD = 24
    NWD = 25

    def __str__(self):
        return self.name


# x and y coordinates in two-dimensional space
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.key = (x, y, z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other: Self):
        return not self.__eq__(other)

    def __lt__(self, other: Self):
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)

    def __str__(self):
        return f"Point {self.x} {self.y} {self.z}"

    def __repr__(self):
        return f"Point {self.x} {self.y} {self.z}"

    def __sub__(self, other: Self) -> Self:
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __hash__(self):
        return hash(self.key)

    # multiply both components of a point by a given number
    def mul(self, n: int) -> Self:
        return Point(n * self.x, n * self.y, n * self.z)

    # Manhattan metric of the point
    def norm(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)


# the origin of the two-dimensional space
origin = Point(0, 0, 0)


# distance between two points using the Manhattan metric
def distance(p1: Point, p2: Point) -> int:
    return (p1 - p2).norm()


# the point one unit from the origin in the given direction
def one_step(direction: Direction) -> Point:
    steps = {
        Direction.N: Point(0, 1, 0),
        Direction.NE: Point(1, 1, 0),
        Direction.E: Point(1, 0, 0),
        Direction.SE: Point(1, -1, 0),
        Direction.S: Point(0, -1, 0),
        Direction.SW: Point(-1, -1, 0),
        Direction.W: Point(-1, 0, 0),
        Direction.NW: Point(-1, 1, 0),

        Direction.U: Point(0, 0, 1),
        Direction.NU: Point(0, 1, 1),
        Direction.NEU: Point(1, 1, 1),
        Direction.EU: Point(1, 0, 1),
        Direction.SEU: Point(1, -1, 1),
        Direction.SU: Point(0, -1, 1),
        Direction.SWU: Point(-1, -1, 1),
        Direction.WU: Point(-1, 0, 1),
        Direction.NWU: Point(-1, 1, 1),

        Direction.D: Point(0, 0, -1),
        Direction.ND: Point(0, 1, -1),
        Direction.NED: Point(1, 1, -1),
        Direction.ED: Point(1, 0, -1),
        Direction.SED: Point(1, -1, -1),
        Direction.SD: Point(0, -1, -1),
        Direction.SWD: Point(-1, -1, -1),
        Direction.WD: Point(-1, 0, -1),
        Direction.NWD: Point(-1, 1, -1),
    }
    return steps[direction]


def get_neighbours(point: Point, grid: dict[Point, str],
                   diagonal: bool = True, corners: bool = True) -> list[str]:
    n = point + one_step(Direction.N)
    ne = point + one_step(Direction.NE)
    e = point + one_step(Direction.E)
    se = point + one_step(Direction.SE)
    s = point + one_step(Direction.S)
    sw = point + one_step(Direction.SW)
    w = point + one_step(Direction.W)
    nw = point + one_step(Direction.NW)

    u = point + one_step(Direction.U)
    nu = point + one_step(Direction.NU)
    nwu = point + one_step(Direction.NEU)
    wu = point + one_step(Direction.EU)
    swu = point + one_step(Direction.SEU)
    su = point + one_step(Direction.SU)
    seu = point + one_step(Direction.SWU)
    eu = point + one_step(Direction.WU)
    neu = point + one_step(Direction.NWU)

    d = point + one_step(Direction.D)
    nd = point + one_step(Direction.ND)
    nwd = point + one_step(Direction.NED)
    wd = point + one_step(Direction.ED)
    swd = point + one_step(Direction.SED)
    sd = point + one_step(Direction.SD)
    sed = point + one_step(Direction.SWD)
    ed = point + one_step(Direction.WD)
    ned = point + one_step(Direction.NWD)

    def add_to_neighbour(p, g):
        return g[p] if is_in_grid(p, g) else None

    neighbours = list()
    neighbours.append(add_to_neighbour(n, grid))
    neighbours.append(add_to_neighbour(e, grid))
    neighbours.append(add_to_neighbour(s, grid))
    neighbours.append(add_to_neighbour(w, grid))
    neighbours.append(add_to_neighbour(u, grid))
    neighbours.append(add_to_neighbour(d, grid))
    if diagonal:
        neighbours.append(add_to_neighbour(ne, grid))
        neighbours.append(add_to_neighbour(nw, grid))
        neighbours.append(add_to_neighbour(se, grid))
        neighbours.append(add_to_neighbour(sw, grid))

        neighbours.append(add_to_neighbour(nu, grid))
        neighbours.append(add_to_neighbour(wu, grid))
        neighbours.append(add_to_neighbour(su, grid))
        neighbours.append(add_to_neighbour(eu, grid))
        neighbours.append(add_to_neighbour(nd, grid))
        neighbours.append(add_to_neighbour(wd, grid))
        neighbours.append(add_to_neighbour(sd, grid))
        neighbours.append(add_to_neighbour(ed, grid))
    if corners:
        neighbours.append(add_to_neighbour(nwu, grid))
        neighbours.append(add_to_neighbour(swu, grid))
        neighbours.append(add_to_neighbour(seu, grid))
        neighbours.append(add_to_neighbour(neu, grid))
        neighbours.append(add_to_neighbour(nwd, grid))
        neighbours.append(add_to_neighbour(swd, grid))
        neighbours.append(add_to_neighbour(sed, grid))
        neighbours.append(add_to_neighbour(ned, grid))


    return [neighbour for neighbour in neighbours if neighbour is not None]


def get_neighbours_dict(point: Point, grid: dict[Point, str],
                        diagonal: bool = True, corners: bool = True) -> dict[Point, str]:
    n = point + one_step(Direction.N)
    ne = point + one_step(Direction.NE)
    e = point + one_step(Direction.E)
    se = point + one_step(Direction.SE)
    s = point + one_step(Direction.S)
    sw = point + one_step(Direction.SW)
    w = point + one_step(Direction.W)
    nw = point + one_step(Direction.NW)

    u = point + one_step(Direction.U)
    nu = point + one_step(Direction.NU)
    nwu = point + one_step(Direction.NEU)
    wu = point + one_step(Direction.EU)
    swu = point + one_step(Direction.SEU)
    su = point + one_step(Direction.SU)
    seu = point + one_step(Direction.SWU)
    eu = point + one_step(Direction.WU)
    neu = point + one_step(Direction.NWU)

    d = point + one_step(Direction.D)
    nd = point + one_step(Direction.ND)
    nwd = point + one_step(Direction.NED)
    wd = point + one_step(Direction.ED)
    swd = point + one_step(Direction.SED)
    sd = point + one_step(Direction.SD)
    sed = point + one_step(Direction.SWD)
    ed = point + one_step(Direction.WD)
    ned = point + one_step(Direction.NWD)

    neighbours = dict()
    neighbours[n] = None if not is_in_grid(n, grid) else grid[n]
    neighbours[e] = None if not is_in_grid(e, grid) else grid[e]
    neighbours[s] = None if not is_in_grid(s, grid) else grid[s]
    neighbours[w] = None if not is_in_grid(w, grid) else grid[w]
    neighbours[u] = None if not is_in_grid(u, grid) else grid[u]
    neighbours[d] = None if not is_in_grid(d, grid) else grid[d]
    if diagonal:
        neighbours[ne] = None if not is_in_grid(ne, grid) else grid[ne]
        neighbours[nw] = None if not is_in_grid(nw, grid) else grid[nw]
        neighbours[se] = None if not is_in_grid(se, grid) else grid[se]
        neighbours[sw] = None if not is_in_grid(sw, grid) else grid[sw]

        neighbours[nu] = None if not is_in_grid(nu, grid) else grid[nu]
        neighbours[wu] = None if not is_in_grid(wu, grid) else grid[wu]
        neighbours[su] = None if not is_in_grid(su, grid) else grid[su]
        neighbours[eu] = None if not is_in_grid(eu, grid) else grid[eu]
        neighbours[nd] = None if not is_in_grid(nd, grid) else grid[nd]
        neighbours[wd] = None if not is_in_grid(wd, grid) else grid[wd]
        neighbours[sd] = None if not is_in_grid(sd, grid) else grid[sd]
        neighbours[ed] = None if not is_in_grid(ed, grid) else grid[ed]
    if corners:
        neighbours[nwu] = None if not is_in_grid(nwu, grid) else grid[nwu]
        neighbours[swu] = None if not is_in_grid(swu, grid) else grid[swu]
        neighbours[seu] = None if not is_in_grid(seu, grid) else grid[seu]
        neighbours[neu] = None if not is_in_grid(neu, grid) else grid[neu]
        neighbours[nwd] = None if not is_in_grid(nwd, grid) else grid[nwd]
        neighbours[swd] = None if not is_in_grid(swd, grid) else grid[swd]
        neighbours[sed] = None if not is_in_grid(sed, grid) else grid[sed]
        neighbours[ned] = None if not is_in_grid(ned, grid) else grid[ned]

    return {key: value for key, value in neighbours.items() if value is not None}


def is_in_grid(point: Point, grid: dict[Point, str]) -> bool:
    return point in grid.keys()


def grid_dimensions(grid: dict[Point, str]):
    xs = [p.x for p in grid.keys()]
    ys = [p.y for p in grid.keys()]
    zs = [p.z for p in grid.keys()]

    nwu = Point(min(xs), max(ys), max(zs))
    sed = Point(max(xs), min(ys), min(zs))

    return nwu, sed


def points_to_text(grid):
    # Find the maximum and minimum coordinates to determine the size of the grid
    g_bounds = grid_dimensions(grid)
    max_x = g_bounds[1].x
    min_x = g_bounds[0].x
    max_y = g_bounds[0].y
    min_y = g_bounds[1].y
    max_z = g_bounds[0].z
    min_z = g_bounds[1].z

    all_text = []
    print(min_z, max_z)
    for z in range(min_z, max_z + 1, 1):
        # Initialize an empty grid with spaces
        text_grid = [[' ' for _ in range(abs(max_x - min_x) + 1)] for _ in range(abs(max_y - min_y) + 1)]

        # Populate the grid with characters from the given points
        for point, char in grid.items():
            if point.z == z:
                x = abs(max_x - min_x) - abs(point.x - max_x)
                y = abs(max_y - min_y) - abs(point.y - max_y)
                text_grid[y][x] = char

        # Convert the grid to a string
        text_level = '\n'.join(''.join(row) for row in reversed(text_grid))
        all_text.append(text_level)

    return all_text


def points_to_text_border(grid):
    # Find the maximum and minimum coordinates to determine the size of the grid
    g_bounds = grid_dimensions(grid)
    max_x = g_bounds[1].x
    min_x = g_bounds[0].x
    max_y = g_bounds[0].y
    min_y = g_bounds[1].y
    max_z = g_bounds[0].z
    min_z = g_bounds[1].z

    all_text = []
    for z in range(min_z, max_z + 1, 1):
        # Initialize an empty grid with spaces
        text_grid = [[' ' for _ in range(abs(max_x - min_x) + 3)] for _ in range(abs(max_y - min_y) + 3)]

        # horizontal borders
        text_grid[0] = ['-'] * (abs(max_x - min_x) + 3)
        text_grid[-1] = ['-'] * (abs(max_x - min_x) + 3)

        # vertical borders
        for index in range(len(text_grid)):
            text_grid[index][0] = '|'
            text_grid[index][-1] = '|'

        # corners
        text_grid[0][0] = '└'
        text_grid[0][-1] = '┘'
        text_grid[-1][0] = '┌'
        text_grid[-1][-1] = '┐'

        # Populate the grid with characters from the given points
        for point, char in grid.items():
            if point.z == z:
                x = abs(max_x - min_x) - abs(point.x - max_x)
                y = abs(max_y - min_y) - abs(point.y - max_y)
                text_grid[y + 1][x + 1] = char
                # text_grid[y + 1][x + 1] = chr(int(char))
                # text_grid[y + 1][x + 1] = 'X'

        # Convert the grid to a string
        text_level = '\n'.join(''.join(row) for row in reversed(text_grid))
        all_text.append(text_level)

    return all_text


def grid_position(char: str, grid: dict[Point, str]):
    return [key for key, value in grid.items() if value == char]
