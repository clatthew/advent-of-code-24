from src.day_4 import Vector, get_matrix, unit_vectors

unit_vectors = {
    int(key / 2): value for key, value in unit_vectors.items() if key % 2 == 0
}


def get_start_pos(map: list[list]) -> Vector | None:
    for y, row in enumerate(map):
        if "^" in row:
            return Vector(row.index("^"), y)


def next_cell(map: list[list], current_position: Vector, current_direction: int) -> str:
    return (current_position + unit_vectors[current_direction]).index(map)


def get_next_position(
    map: list[list], current_position: Vector, current_direction: int
) -> Vector:
    while next_cell(map, current_position, current_direction) == "#":
        current_direction = (current_direction + 1) % 4
    return current_position + unit_vectors[current_direction], current_direction


def task_1():
    map = get_matrix("input/6.txt")
    current_position: Vector = get_start_pos(map)
    current_direction: int = 3
    no_places_visited: int = -1
    while True:
        if current_position.index(map) != "X":
            no_places_visited += 1
            current_position.set_value(map, "X")
        try:
            current_position, current_direction = get_next_position(
                map, current_position, current_direction
            )
        except IndexError:
            break
    return no_places_visited


def task_2():
    pass


if __name__ == "__main__":
    pass
