from collections import deque
import heapq
from typing import Callable
from utils.geometry import *


def bfs(start: Point, goal: Point, grid: dict[Point, str],
        is_valid_move: Callable[[str, str], bool] = lambda x, y: True, diagonal: bool = False) -> list[Point]:
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbours_dict(current, grid, diagonal=diagonal)
        for neighbor, value in neighbors.items():
            if neighbor not in visited and is_valid_move(grid[current], value):
                queue.append((neighbor, path + [neighbor]))

    # If no path is found
    return []


def dfs(start: Point, goal: Point, grid: dict[Point, str],
        is_valid_move: Callable[[str, str], bool] = lambda x, y: True, diagonal: bool = False) -> list[Point]:
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbours_dict(current, grid, diagonal=diagonal)
        for neighbor, value in neighbors.items():
            if neighbor not in visited and is_valid_move(grid[current], value):
                stack.append((neighbor, path + [neighbor]))

    # If no path is found
    return []


def dijkstra(start: Point, goal: Point, grid: dict[Point, str],
             is_valid_move: Callable[[str, str], bool] = lambda x, y: True, diagonal: bool = False) -> (list[Point], set[Point]):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        current_distance, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, visited

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbours_dict(current, grid, diagonal=diagonal)
        for neighbor, value in neighbors.items():
            if neighbor not in visited and is_valid_move(grid[current], value):
                new_distance = current_distance + 1  # Assuming unit cost for each step
                heapq.heappush(priority_queue, (new_distance, neighbor, path + [neighbor]))

    # If no path is found
    return [], visited