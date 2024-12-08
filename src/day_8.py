from src.day_5 import add_to_dict
from src.day_4 import Vector
from typing import Callable

TOP_LEFT = Vector(0, 0)


def prepare_input(filepath: str) -> tuple[Vector, dict[str, list[Vector]]]:
    antennae = {}
    with open(filepath) as f:
        for y, line in enumerate(f):
            for x, cell in enumerate(line.strip()):
                bottom_corner = Vector(x, y)
                if cell != ".":
                    add_to_dict(antennae, cell, Vector(x, y))
    return bottom_corner, antennae


def relative_vector_of(location_1: Vector, location_2: Vector) -> Vector:
    """return the vector pointing from location_2 to location_1"""
    return location_1 - location_2


def antinodes_of_pair_1(
    location_1: Vector, location_2: Vector, bottom_right: Vector
) -> list[Vector]:
    relative_vector = relative_vector_of(location_1, location_2)
    candidates = [location_1 + relative_vector, location_2 - relative_vector]
    return [
        location
        for location in candidates
        if location.is_enclosed_by(TOP_LEFT, bottom_right)
    ]


def antinodes_of_pair_2(
    location_1: Vector, location_2: Vector, bottom_right: Vector
) -> list[Vector]:
    relative_vector = relative_vector_of(location_1, location_2)
    candidates = []
    for direction in [1, -1]:
        antinode_position = location_1
        while antinode_position.is_enclosed_by(TOP_LEFT, bottom_right):
            candidates.append(antinode_position)
            antinode_position += relative_vector * direction
    return candidates


def find_antinodes(
    antenna_locations: list[Vector],
    pair_function: Callable[[Vector, Vector, Vector], list[Vector]],
    bottom_right: Vector,
) -> list[Vector]:
    antinode_locations = []
    for i, location_1 in enumerate(antenna_locations[:-1]):
        for location_2 in antenna_locations[i + 1 :]:
            antinode_locations += pair_function(location_1, location_2, bottom_right)
    return antinode_locations


PAIR_FUNCTIONS = {1: antinodes_of_pair_1, 2: antinodes_of_pair_2}


def tasks(filepath: str = "input/8.txt", task: int = 1) -> int:
    bottom_right, antennae_locations = prepare_input(filepath)
    all_antinode_locations = []
    for _, locations in antennae_locations.items():
        candidates = find_antinodes(locations, PAIR_FUNCTIONS[task], bottom_right)
        for location in candidates:
            if location not in all_antinode_locations:
                all_antinode_locations.append(location)
    return len(all_antinode_locations)
