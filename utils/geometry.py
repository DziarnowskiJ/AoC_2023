from enum import Enum
from typing_extensions import Self


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

    def __str__(self):
        return self.name


# the direction immediately to the left
def turn_left(direction: Direction) -> Direction:
    left_turns = [Direction.W, Direction.NW, Direction.N, Direction.NE, Direction.E, Direction.SE, Direction.S, Direction.SW]
    return left_turns[(direction.value - 1) % 8]


# the direction immediately to the right
def turn_right(direction: Direction) -> Direction:
    right_turns = [Direction.E, Direction.SE, Direction.S, Direction.SW, Direction.W, Direction.NW, Direction.N, Direction.NE]
    return right_turns[(direction.value + 1) % 8]


# x and y coordinates in two-dimensional space
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.key = (x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Self):
        return not self.__eq__(other)

    def __lt__(self, other: Self):
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self):
        return f"Point {self.x} {self.y}"

    def __repr__(self):
        return f"Point {self.x} {self.y}"

    def __sub__(self, other: Self) -> Self:
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash(self.key)

    # multiply both components of a point by a given number
    def mul(self, n: int) -> Self:
        return Point(n * self.x, n * self.y)

    # Manhattan metric of the point
    def norm(self) -> int:
        return abs(self.x) + abs(self.y)


# the origin of the two-dimensional space
origin = Point(0, 0)


# distance between two points using the Manhattan metric
def distance(p1: Point, p2: Point) -> int:
    return (p1 - p2).norm()


# the point one unit from the origin in the given direction
def one_step(direction: Direction) -> Point:
    steps = {
        Direction.N: Point(0, 1),
        Direction.NE: Point(1, 1),
        Direction.E: Point(1, 0),
        Direction.SE: Point(1, -1),
        Direction.S: Point(0, -1),
        Direction.SW: Point(-1, -1),
        Direction.W: Point(-1, 0),
        Direction.NW: Point(-1, 1),
    }
    return steps[direction]


def read_grid(text_grid: str, origin: Direction = Direction.NE) -> [(Point, str)]:
    lines_of_text = text_grid.split('\n')
    if origin == Direction.NE:
        return [(Point(x, -y), c) for y, line in enumerate(lines_of_text)
                for x, c in enumerate(line)]
    elif origin == Direction.NW:
        return [(Point(-x, -y), c) for y, line in enumerate(lines_of_text)
                for x, c in enumerate(reversed(line))]
    elif origin == Direction.SE:
        return [(Point(x, y - 1), c) for y, line in enumerate(reversed(lines_of_text))
                for x, c in enumerate(line)]
    elif origin == Direction.SW:
        return [(Point(-x, y - 1), c) for y, line in enumerate(reversed(lines_of_text))
                for x, c in enumerate(reversed(line))]
    else:
        raise Exception("origin can only be NE, NW, SE or SW")


def grid_dict(text_grid: str, origin: Direction = Direction.NE) -> dict[Point, str]:
    lines_of_text = text_grid.split('\n')
    if origin == Direction.NE:
        return {Point(x, -y): c for y, line in enumerate(lines_of_text)
                for x, c in enumerate(line)}
    elif origin == Direction.NW:
        return {Point(-x, -y): c for y, line in enumerate(lines_of_text)
                for x, c in enumerate(reversed(line))}
    elif origin == Direction.SE:
        return {Point(x, y - 1): c for y, line in enumerate(reversed(lines_of_text))
                for x, c in enumerate(line)}
    elif origin == Direction.SW:
        return {Point(-x, y - 1): c for y, line in enumerate(reversed(lines_of_text))
                for x, c in enumerate(reversed(line))}
    else:
        raise Exception("origin can only be NE, NW, SE or SW")


def get_neighbours(point: Point, grid: dict[Point, str],
                   diagonal: bool = True) -> list[str]:
    n = point + one_step(Direction.N)
    ne = point + one_step(Direction.NE)
    e = point + one_step(Direction.E)
    se = point + one_step(Direction.SE)
    s = point + one_step(Direction.S)
    sw = point + one_step(Direction.SW)
    w = point + one_step(Direction.W)
    nw = point + one_step(Direction.NW)

    def add_to_neighbour(p, g):
        return g[p] if is_in_grid(p, g) else None

    neighbours = list()
    neighbours.append(add_to_neighbour(n, grid))
    neighbours.append(add_to_neighbour(e, grid))
    neighbours.append(add_to_neighbour(s, grid))
    neighbours.append(add_to_neighbour(w, grid))
    if diagonal:
        neighbours.append(add_to_neighbour(ne, grid))
        neighbours.append(add_to_neighbour(nw, grid))
        neighbours.append(add_to_neighbour(se, grid))
        neighbours.append(add_to_neighbour(sw, grid))

    return [neighbour for neighbour in neighbours if neighbour is not None]


def get_neighbours_dict(point: Point, grid: dict[Point, str],
                        diagonal: bool = True) -> dict[Point, str]:
    n = point + one_step(Direction.N)
    ne = point + one_step(Direction.NE)
    e = point + one_step(Direction.E)
    se = point + one_step(Direction.SE)
    s = point + one_step(Direction.S)
    sw = point + one_step(Direction.SW)
    w = point + one_step(Direction.W)
    nw = point + one_step(Direction.NW)

    neighbours = dict()
    neighbours[n] = None if not is_in_grid(n, grid) else grid[n]
    neighbours[e] = None if not is_in_grid(e, grid) else grid[e]
    neighbours[s] = None if not is_in_grid(s, grid) else grid[s]
    neighbours[w] = None if not is_in_grid(w, grid) else grid[w]
    if diagonal:
        neighbours[ne] = None if not is_in_grid(ne, grid) else grid[ne]
        neighbours[nw] = None if not is_in_grid(nw, grid) else grid[nw]
        neighbours[se] = None if not is_in_grid(se, grid) else grid[se]
        neighbours[sw] = None if not is_in_grid(sw, grid) else grid[sw]

    return {key: value for key, value in neighbours.items() if value is not None}


def is_in_grid(point: Point, grid: dict[Point, str]) -> bool:
    return point in grid.keys()


def grid_dimensions(grid: dict[Point, str]):
    xs = [p.x for p in grid.keys()]
    ys = [p.y for p in grid.keys()]

    top_left = Point(min(xs), max(ys))
    bottom_right = Point(max(xs), min(ys))

    return top_left, bottom_right

def grid_position(char: str, grid: dict[Point, str]):
    return [key for key, value in grid.items() if value == char]

def points_to_text(grid):
    # Find the maximum and minimum coordinates to determine the size of the grid
    g_bounds = grid_dimensions(grid)
    max_x = g_bounds[1].x
    min_x = g_bounds[0].x
    max_y = g_bounds[0].y
    min_y = g_bounds[1].y

    # Initialize an empty grid with spaces
    text_grid = [[' ' for _ in range(abs(max_x - min_x) + 1)] for _ in range(abs(max_y - min_y) + 1)]

    # Populate the grid with characters from the given points
    for point, char in grid.items():
        x = abs(max_x - min_x) - abs(point.x - max_x)
        y = abs(max_y - min_y) - abs(point.y - max_y)
        text_grid[y][x] = char

    # Convert the grid to a string
    text = '\n'.join(''.join(row) for row in reversed(text_grid))

    return text

def empty_grid(nw_point, se_point, char = '.'):
    grid = dict()
    for i in range(nw_point.x,se_point.x + 1, 1):
        for j in range(nw_point.y, se_point.y - 1, -1):
            grid[Point(i, j)] = char
    return grid