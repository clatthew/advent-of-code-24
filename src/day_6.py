from src.day_4 import Vector, get_matrix, unit_vectors
from copy import deepcopy

unit_vectors = {
    int(key / 2): value for key, value in unit_vectors.items() if key % 2 == 0
}


def str_to_Vector(vector: str):
    vector_list = [int(i) for i in vector[1:-1].split(",")]
    return Vector(vector_list[0], vector_list[1])


def get_start_pos(map: list[list]) -> Vector | None:
    for y, row in enumerate(map):
        if "^" in row:
            return Vector(row.index("^"), y)


def next_cell(map: list[list], current_position: Vector, current_direction: int) -> str:
    next_cell = current_position + unit_vectors[current_direction]
    if next_cell.is_inside_of(map):
        return (next_cell).index(map)
    return False


def get_next_position(
    map: list[list], current_position: Vector, current_direction: int
) -> Vector:
    moved = False
    while not moved:
        next_pos_candidate = next_cell(map, current_position, current_direction)
        if not next_pos_candidate:
            raise IndexError
        if next_pos_candidate == "#":
            current_direction = (current_direction + 1) % 4
        else:
            moved = True
    return current_position + unit_vectors[current_direction], current_direction


def is_periodic(visits: list):
    return len(visits) > 4


def places_visited(map: list[list]) -> dict:
    current_position: Vector = get_start_pos(map)
    current_direction: int = 3
    places_visited = {}
    steps = 0
    periodic = False
    while current_position.is_inside_of(map):
        try:
            current_position, current_direction = get_next_position(
                map, current_position, current_direction
            )
        except IndexError:
            break
        if str(current_position) not in places_visited:
            places_visited[str(current_position)] = [steps]
        else:
            places_visited[str(current_position)].append(steps)
            if is_periodic(places_visited[str(current_position)]):
                periodic = True
                break
        steps += 1
    if periodic:
        return "periodic"
    return places_visited


def task_1(map=get_matrix("input/6.txt")):
    return len(places_visited(map)) - 1


def task_2(map=get_matrix("input/6.txt")):
    guard_positions = places_visited(map)
    del guard_positions[str(get_start_pos(map))]
    loop_positions = 0
    for position in list(guard_positions):
        position = str_to_Vector(position)
        modified_map = deepcopy(map)
        position.set_value(modified_map, "#")
        if places_visited(modified_map) == "periodic":
            loop_positions += 1
    return loop_positions
