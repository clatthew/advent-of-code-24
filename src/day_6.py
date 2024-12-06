from src.day_4 import Vector, get_matrix, unit_vectors
from copy import deepcopy

unit_vectors = {
    int(key / 2): value for key, value in unit_vectors.items() if key % 2 == 0
}


class Periodic(Exception):
    pass


def get_start_pos(map: list[list]) -> Vector | None:
    for y, row in enumerate(map):
        if "^" in row:
            return Vector(row.index("^"), y)


def next_cell(map: list[list], current_position: Vector, current_direction: int) -> str:
    next_cell = current_position + unit_vectors[current_direction]
    if next_cell.is_inside_of(map):
        return next_cell.index(map)
    raise IndexError


def get_next_position(
    map: list[list], current_position: Vector, current_direction: int
) -> Vector:
    while next_cell(map, current_position, current_direction) == "#":
        current_direction = (current_direction + 1) % 4
    return current_position + unit_vectors[current_direction], current_direction


def is_periodic(visits: list):
    return len(visits) > 4


def places_visited(map: list[list]) -> dict:
    current_position: Vector = get_start_pos(map)
    current_direction: int = 3
    places_visited = {}
    steps = 0
    while True:
        try:
            current_position, current_direction = get_next_position(
                map, current_position, current_direction
            )
        except IndexError:
            break
        if current_position.as_tuple not in places_visited:
            places_visited[current_position.as_tuple] = [steps]
        else:
            places_visited[current_position.as_tuple].append(steps)
            if is_periodic(places_visited[current_position.as_tuple]):
                raise Periodic
        steps += 1
    return places_visited


def task_1(map: list[list] = get_matrix("input/6.txt")):
    return len(places_visited(map)) - 1


def task_2(map: list[list] = get_matrix("input/6.txt")):
    guard_positions = places_visited(map)
    del guard_positions[get_start_pos(map).as_tuple]
    loop_positions = 0
    for position in guard_positions:
        modified_map = deepcopy(map)
        Vector(*position).set_value(modified_map, "#")
        try:
            places_visited(modified_map)
        except Periodic:
            loop_positions += 1
    return loop_positions
