from src.day_4 import Vector, matrix_iterator
from src.day_6 import unit_vectors
from src.day_10 import remove_duplicates
from copy import copy


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

    # goes wrong with a single concave piece
    # need categorisation algorithm where each group only contains a straight line of points
    # write an algorithm that can trace around the outside of the shape?
    @property
    def no_of_sides(self) -> int:
        adjacents: list[Vector] = []
        for plot in self.plots:
            for _, direction in unit_vectors.items():
                neighbour = plot + direction
                if neighbour not in adjacents + self.plots:
                    adjacents.append(neighbour)
        print(
            f"region: {self.letter} adjacents: {[i.as_tuple for i in sorted(adjacents, key=lambda x: x.y)]}"
        )
        groups = []
        for new_adj in sort_list_of_vectors(adjacents):
            groups = categorise(groups, new_adj)
        no_of_sides = 0
        for group in groups:
            group_sides = []
            for vector in group:
                for i, direction in unit_vectors.items():
                    if vector + direction in self.plots:
                        group_sides.append(i)
            no_of_sides += len(remove_duplicates(group_sides))
            print(
                f"group: {[i.as_tuple for i in group]} sides: {len(remove_duplicates(group_sides))}"
            )
        print(f"region: {self.letter} sides: {no_of_sides}")
        return no_of_sides

    @property
    def cost_1(self):
        return self.perimeter * self.area

    @property
    def cost_2(self):
        return self.no_of_sides * self.area


def categorise(groups: list[list[Vector]], adjacent: Vector):
    for group in groups:
        if len(group) > 1:
            if adjacent == group[-1] * 2 - group[-2]:
                group.append(adjacent)
                return groups
        else:
            if adjacent.is_adjacent_to(group[0]):
                group.append(adjacent)
                return groups
    groups.append([adjacent])
    return groups


def sort_list_of_vectors(vector_list: list[Vector]) -> list[Vector]:
    # print(f"original: {[i.as_tuple for i in vector_list]}")
    for i, _ in enumerate(vector_list):
        for j, _ in enumerate(vector_list[i + 1 :], i + 1):
            if compare_vectors(vector_list[i], vector_list[j]):
                placeholder = vector_list[j]
                vector_list[j] = vector_list[i]
                vector_list[i] = placeholder
    # print(f"sorted  : {[i.as_tuple for i in vector_list]}")
    return vector_list


def compare_vectors(a: Vector, b: Vector) -> bool:
    if a.x > b.x:
        return True
    elif a.x == b.x:
        return a.y > b.y
    return False


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
