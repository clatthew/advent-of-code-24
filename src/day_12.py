from src.day_4 import Vector, matrix_iterator
from src.day_6 import unit_vectors


class Region:
    def __init__(self, plots: list[Vector], letter: str):
        self.plots = plots
        self.letter = letter

    @property
    def area(self) -> int:
        return len(self.plots)

    @property
    def perimeter(self) -> int:
        perimiter = 0
        for plot in self.plots:
            for _, direction in unit_vectors.items():
                if plot + direction not in self.plots:
                    perimiter += 1
        return perimiter

    @property
    def no_of_sides(self) -> int:
        adjacents: list[Vector] = []
        for plot in self.plots:
            for _, direction in unit_vectors.items():
                neighbour = plot + direction
                if neighbour not in adjacents + self.plots:
                    adjacents.append(neighbour)
        direction_changes = 0
        while adjacents:
            start_position = adjacents[0]
            for i, direction in unit_vectors.items():
                if start_position + direction in self.plots:
                    start_direction = (i + 3) % 4
            adjacents_in_loop = [start_position]
            directions_in_loop = [start_direction]
            next_position, next_direction = self.next_step(
                start_position, start_direction
            )
            while (next_position, next_direction) != (start_position, start_direction):
                adjacents_in_loop.append(next_position)
                directions_in_loop.append(next_direction)
                next_position, next_direction = self.next_step(
                    next_position, next_direction
                )
            adjacents_in_loop.append(next_position)
            directions_in_loop.append(next_direction)
            for adjacent in adjacents_in_loop:
                try:
                    adjacents.remove(adjacent)
                except ValueError:
                    pass
            for i, j in zip(directions_in_loop[:-1], directions_in_loop[1:]):
                if i != j:
                    direction_changes += 1
        return direction_changes

    def next_step(self, position: Vector, direction: int) -> tuple[Vector, int]:
        if position + unit_vectors[direction] in self.plots:
            return position, (direction + 3) % 4
        if (
            position + unit_vectors[direction] + unit_vectors[(direction + 1) % 4]
            in self.plots
        ):
            return position + unit_vectors[direction], direction
        return position + unit_vectors[direction] + unit_vectors[(direction + 1) % 4], (
            direction + 1
        ) % 4

    @property
    def cost_1(self):
        return self.perimeter * self.area

    @property
    def cost_2(self):
        return self.no_of_sides * self.area


class Solution:
    def __init__(self, map: list[list]):
        self.regions = self.find_regions(map)

    def find_regions(self, map: list[list]) -> list[Region]:
        regions = []
        for _, position in matrix_iterator(map):
            position_name = position.index(map)
            if position_name:
                regions.append(
                    Region(self.region_containing(position, map), position_name)
                )
        return regions

    def region_containing(self, position: Vector, map: list[list]) -> list[Vector]:
        plots = [position]
        position_type = position.index(map)
        position.set_value(map, None)
        for _, direction in unit_vectors.items():
            neighbour: Vector = position + direction
            if neighbour.index(map, True) == position_type:
                plots += self.region_containing(neighbour, map)
        return plots
