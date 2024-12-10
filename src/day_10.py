from src.day_4 import get_matrix, Vector
from src.day_6 import unit_vectors


def add_to_unique_list(target_list: list, new_items: list) -> list:
    for item in new_items:
        if item not in target_list:
            target_list.append(item)
    return target_list


class Solution:
    def __init__(self, filepath: str = "input/10.txt"):
        self.map = [[int(j) for j in i] for i in get_matrix(filepath)]

    @property
    def score_function(self):
        if self.task == 1:
            return self.no_possible_summits_from
        else:
            return self.no_possible_paths_from

    def task(self, task: int = 1) -> int:
        self.task = task
        total_score = 0
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if not cell:
                    total_score += self.score_function(Vector(x, y))
        return total_score

    def no_possible_summits_from(self, position: Vector) -> int:
        return len(self.possible_summits_from(position))

    def possible_summits_from(self, position: Vector) -> list[Vector]:
        if position.index(self.map) == 9:
            return [position]
        summits = []
        for _, direction in unit_vectors.items():
            next_step = position + direction
            if next_step.is_inside_of(self.map):
                if position.index(self.map) + 1 == next_step.index(self.map):
                    summits = add_to_unique_list(
                        summits, self.possible_summits_from(next_step)
                    )
        return summits

    def no_possible_paths_from(self, position: Vector) -> int:
        if position.index(self.map) == 9:
            return 1
        paths = 0
        for _, direction in unit_vectors.items():
            next_step = position + direction
            if next_step.is_inside_of(self.map):
                if position.index(self.map) + 1 == next_step.index(self.map):
                    paths += self.no_possible_paths_from(next_step)
        return paths
