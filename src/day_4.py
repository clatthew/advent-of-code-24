from typing import Self


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return str(self.as_tuple)

    @property
    def as_tuple(self) -> tuple:
        return (self.x, self.y)

    def __eq__(self, other: Self) -> bool:
        return self.as_tuple == other.as_tuple

    @property
    def is_negative(self):
        return self.x < 0 or self.y < 0

    def index(self, matrix: list[list]):
        return matrix[self.y][self.x]

    def is_inside_of(self, matrix: list[list]):
        if self.is_negative:
            return False
        if self.y > len(matrix):
            return False
        if self.x > len(matrix[0]):
            return False
        return True

    def is_enclosed_by(self, top_left: Self, bottom_right: Self) -> bool:
        for component in ["x", "y"]:
            if (
                not getattr(top_left, component)
                <= getattr(self, component)
                <= getattr(bottom_right, component)
            ):
                return False
        return True

    def set_value(self, matrix: list[list], new_value):
        matrix[self.y][self.x] = new_value


unit_vectors = {
    0: Vector(1, 0),
    1: Vector(1, 1),
    2: Vector(0, 1),
    3: Vector(-1, 1),
    4: Vector(-1, 0),
    5: Vector(-1, -1),
    6: Vector(0, -1),
    7: Vector(1, -1),
}


def read_file(filepath: str):
    with open(filepath, "r") as f:
        yield from f


def get_matrix(filepath: str = "input/4.txt"):
    matrix = []
    for line in read_file(filepath):
        matrix.append(list(line))
    return matrix


def follow_direction(
    matrix: list[list[str]], start_point: Vector, direction: int, word_length: int = 4
) -> list:
    word = ""
    for _ in range(word_length):
        if start_point.is_negative:
            return None
        try:
            word += start_point.index(matrix)
            start_point += unit_vectors[direction]
        except IndexError:
            return None
    return word


def search_word_from_letter(
    matrix: list[list[str]], start_point: Vector, target: str = "XMAS"
):
    count = 0
    for direction in range(8):
        if follow_direction(matrix, start_point, direction) == target:
            count += 1
    return count


def task_1():
    matrix = get_matrix()
    xmas_count = 0
    for y, row in enumerate(matrix):
        for x, letter in enumerate(row):
            if letter == "X":
                start_point = Vector(x, y)
                xmas_count += search_word_from_letter(matrix, start_point)
    return xmas_count


def find_cross(
    matrix: list[list[str]], start_point: Vector, skew: int = 1, target="MAS"
) -> str:
    skews = {0: [Vector(0, 1), Vector(1, 0)], 1: [Vector(1, -1), Vector(1, 1)]}
    try:
        for axis in skews[skew]:
            indices = [start_point - axis, start_point, start_point + axis]
            word = "".join([index.index(matrix) for index in indices])
            if word not in [target, target[::-1]]:
                return False
        return True
    except IndexError:
        return False


def task_2():
    matrix = get_matrix()
    x_mas_count = 0
    for y, row in enumerate(matrix):
        for x, letter in enumerate(row):
            if letter == "A":
                x_mas_count += find_cross(matrix, Vector(x, y))
    return x_mas_count
