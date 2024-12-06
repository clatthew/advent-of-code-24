from src.day_4 import Vector, get_matrix, unit_vectors, follow_direction

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


def width_and_lenth_candidates(map: list[list], position: Vector):
    max_width = len(map[position.y]) - position.x
    horizontal_cells = follow_direction(map, position + Vector(0, 1), 0, max_width)
    try:
        width = horizontal_cells.index("#")
    except ValueError:
        return None
    max_length = len(map) - position.y
    # print(f"position={str(position)}")
    vertical_cells = follow_direction(map, position + Vector(-1, 0), 2, max_length - 2)
    # print(f"{vertical_cells=}")
    try:
        length = vertical_cells.index("#")
    except ValueError:
        return None
    return width, length


def possible_loop_with(map: list[list], position: Vector):
    dimensions = width_and_lenth_candidates(map, position)
    if dimensions:
        width, length = dimensions
    else:
        return False
    # print(f"position={str(position)} {width=} {length=}")
    hashtags = [
        position,
        position + Vector(width, 1),
        position + Vector(width - 1, length + 1),
        position + Vector(-1, length),
    ]

    for corner in hashtags[1:]:
        if corner.index(map) != "#":
            return False

    circuit = (
        follow_direction(map, hashtags[0] + Vector(0, 1), 0, width - 1)
        + follow_direction(map, hashtags[1] + Vector(-1, 0), 2, length - 1)
        + follow_direction(map, hashtags[2] + Vector(0, -1), 4, width - 1)
        + follow_direction(map, hashtags[3] + Vector(1, 0), 6, length - 1)
    )
    if "#" in circuit:
        return False
    return True


def task_2():
    map = get_matrix("input/6.txt")
    loop_positions = 0
    for y, row in enumerate(map[:-2]):
        for x, _ in enumerate(row[1:-1]):
            # loop_positions += check_for_loop(map, Vector(x, y))
            # print(x, y)
            loop_positions += possible_loop_with(map, Vector(x + 1, y))
    return loop_positions


if __name__ == "__main__":
    print(task_2())
