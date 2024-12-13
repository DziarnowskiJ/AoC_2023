from typing import List, Tuple
from collections import deque
from utils.geometry import *

# def flood_fill(grid: dict[Point, str], start_point: Point, fill_char: str) -> dict[Point, str]:
#     """
#     Perform flood fill on a grid starting from the given point.
#
#     Parameters:
#     - grid: A dictionary representing the grid.
#     - start_point: The starting point for the flood fill.
#     - fill_char: The character to fill the connected region with.
#
#     Returns:
#     A new grid with the flooded area filled with the specified character.
#     """
#
#     # Check if the starting point is in the grid
#     if not is_in_grid(start_point, grid):
#         raise ValueError("Starting point is outside the grid.")
#
#     # Create a copy of the original grid to modify
#     new_grid = grid.copy()
#
#     # Initialize the queue for BFS
#     queue = deque([start_point])
#
#     # Define the original character at the starting point
#     original_char = grid[start_point]
#
#     # Keep track of visited points
#     visited = set()
#
#     # Perform BFS until the queue is empty
#     while queue:
#         current_point = queue.popleft()
#
#         # Check if the current point is within the grid, has the original character, and has not been visited
#         if (
#             is_in_grid(current_point, new_grid)
#             and new_grid[current_point] == original_char
#             and current_point not in visited
#         ):
#             # Fill the current point with the new character
#             new_grid[current_point] = fill_char
#
#             # Mark the current point as visited
#             visited.add(current_point)
#
#             # Add neighbors to the queue
#             neighbors = get_neighbours_dict(current_point, new_grid, diagonal=False, vals_only=True)
#             queue.extend(neighbors)
#
#     return new_grid
#
# def flood_fill_all_connected(grid: dict[Point, str], start_point: Point, fill_char: str) -> dict[Point, str]:
#     """
#     Perform flood fill on a grid for all characters connected to the starting point.
#
#     Parameters:
#     - grid: A dictionary representing the grid.
#     - start_point: The starting point for the flood fill.
#     - fill_char: The character to fill the connected regions with.
#
#     Returns:
#     A new grid with all connected regions filled with the specified character.
#     """
#
#     # Create a copy of the original grid to modify
#     new_grid = grid.copy()
#
#     # Perform flood fill from the specified starting point
#     new_grid = flood_fill(new_grid, start_point, fill_char)
#
#     return new_grid

def flood_fill(grid: dict[Point, str], start_point: Point, fill_char: str) -> dict[Point, str]:
    """
    Perform flood fill on a grid starting from the given point.

    Parameters:
    - grid: A dictionary representing the grid.
    - start_point: The starting point for the flood fill.
    - fill_char: The character to fill the connected region with.

    Returns:
    A new grid with the flooded area filled with the specified character.
    """

    # Check if the starting point is in the grid
    if not is_in_grid(start_point, grid):
        raise ValueError("Starting point is outside the grid.")

    # Create a copy of the original grid to modify
    new_grid = grid.copy()

    # Initialize the queue for BFS
    queue = deque([start_point])

    # Keep track of visited points
    visited = set()

    # Perform BFS until the queue is empty
    while queue:
        current_point = queue.popleft()

        # Check if the current point is within the grid and has not been visited
        if is_in_grid(current_point, new_grid) and current_point not in visited:
            # Fill the current point with the new character
            new_grid[current_point] = fill_char

            # Mark the current point as visited
            visited.add(current_point)

            # Add neighbors to the queue
            neighbors = get_neighbours_dict(current_point, new_grid, diagonal=False)
            queue.extend(neighbors)

    return new_grid

def flood_fill_all_connected(grid: dict[Point, str], start_point: Point, fill_char: str) -> dict[Point, str]:
    """
    Perform flood fill on a grid for all characters connected to the starting point.

    Parameters:
    - grid: A dictionary representing the grid.
    - start_point: The starting point for the flood fill.
    - fill_char: The character to fill the connected regions with.

    Returns:
    A new grid with all connected regions filled with the specified character.
    """

    # Create a copy of the original grid to modify
    new_grid = grid.copy()

    # Perform flood fill from the specified starting point
    new_grid = flood_fill(new_grid, start_point, fill_char)

    return new_grid
def create_loop_mask(grid: dict[Point, str], loop_points: List[Point]) -> set[Point]:
    """
    Create a mask to mark the points inside a closed loop.

    Parameters:
    - grid: A dictionary representing the grid.
    - loop_points: A list of points representing a closed loop.

    Returns:
    A set of points inside the loop.
    """
    loop_mask = set()

    # Check if the loop is valid
    if len(loop_points) < 3 or loop_points[0] != loop_points[-1]:
        raise ValueError("Invalid loop. A loop must have at least three points and be closed.")

    # Use the scanline algorithm to mark points inside the loop
    for y in range(min(point.y for point in loop_points), max(point.y for point in loop_points) + 1):
        intersections = []
        for i in range(len(loop_points) - 1):
            if (
                (loop_points[i].y <= y < loop_points[i + 1].y) or
                (loop_points[i + 1].y <= y < loop_points[i].y)
            ):
                x = int((loop_points[i + 1].x - loop_points[i].x) * (y - loop_points[i].y) /
                        (loop_points[i + 1].y - loop_points[i].y) + loop_points[i].x)
                intersections.append(x)

        # Sort the intersections and fill the points between them
        intersections.sort()
        for i in range(0, len(intersections), 2):
            for x in range(intersections[i], intersections[i + 1] + 1):
                loop_mask.add(Point(x, y))

    return loop_mask

def flood_fill_outside_loop(grid: dict[Point, str], loop_points: List[Point], fill_char: str) -> dict[Point, str]:
    """
    Perform flood fill on a grid outside the provided loop of points.

    Parameters:
    - grid: A dictionary representing the grid.
    - loop_points: A list of points representing a closed loop.
    - fill_char: The character to fill the regions outside the loop with.

    Returns:
    A new grid with all regions outside the loop filled with the specified character.
    """

    # Create a copy of the original grid to modify
    new_grid = grid.copy()

    # Create a mask to mark points inside the loop
    loop_mask = create_loop_mask(new_grid, loop_points)

    # Perform flood fill outside the loop
    for point in grid.keys():
        if point not in loop_mask:
            new_grid = flood_fill(new_grid, point, fill_char)

    return new_grid

def my_flood_fill(grid: dict[Point, str], start_point: Point, fill_char: str, skip: [Point]) -> dict[Point, str]:
    """
    Perform flood fill on a grid starting from the given point.

    Parameters:
    - grid: A dictionary representing the grid.
    - start_point: The starting point for the flood fill.
    - fill_char: The character to fill the connected region with.

    Returns:
    A new grid with the flooded area filled with the specified character.
    """

    # Check if the starting point is in the grid
    if not is_in_grid(start_point, grid):
        raise ValueError("Starting point is outside the grid.")

    # Create a copy of the original grid to modify
    new_grid = grid.copy()

    # Initialize the queue for BFS
    queue = deque([start_point])

    # Keep track of visited points
    visited = set()

    # Perform BFS until the queue is empty
    while queue:
        current_point = queue.popleft()

        # Check if the current point is within the grid and has not been visited
        if is_in_grid(current_point, new_grid) and current_point not in visited and current_point not in skip:
            # Fill the current point with the new character
            new_grid[current_point] = fill_char

            # Mark the current point as visited
            visited.add(current_point)

            # Add neighbors to the queue
            neighbors = get_neighbours_dict(current_point, new_grid, diagonal=False, vals_only=True)
            queue.extend(neighbors)

    return new_grid