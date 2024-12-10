from src.day_4 import get_matrix, Vector
from src.day_6 import unit_vectors


def remove_duplicates(target_list: list) -> list:
    new_list = []
    for item in target_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


def matrix_iterator(matrix: list[list]):
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            yield cell, Vector(x, y)


class Solution:
    def __init__(self, filepath: str = "input/10.txt"):
        self.map = [[int(j) for j in i] for i in get_matrix(filepath)]

    def task(self, task: int = 1) -> int:
        self.task = task
        total_score = 0
        for cell, position in matrix_iterator(self.map):
            if not cell:
                total_score += self.no_possible_summits_from(position)
        return total_score

    def no_possible_summits_from(self, position: Vector) -> int:
        if self.task == 1:
            return len(remove_duplicates(self.possible_summits_from(position)))
        return len(self.possible_summits_from(position))

    def possible_summits_from(self, position: Vector) -> list[Vector]:
        if position.index(self.map) == 9:
            return [position]
        summits = []
        for _, direction in unit_vectors.items():
            next_step = position + direction
            if next_step.is_inside_of(self.map):
                if position.index(self.map) + 1 == next_step.index(self.map):
                    summits += self.possible_summits_from(next_step)
        return summits
