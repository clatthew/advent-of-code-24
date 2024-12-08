from src.day_5 import add_to_dict
from src.day_4 import Vector


def prepare_input(filepath: str) -> tuple[Vector, dict[str, list[Vector]]]:
    antennae = {}
    with open(filepath) as f:
        for y, line in enumerate(f):
            for x, cell in enumerate(line.strip()):
                bottom_corner = Vector(x, y)
                if cell != ".":
                    add_to_dict(antennae, cell, Vector(x, y))
    return bottom_corner, antennae


def find_antinodes(antenna_locations: list[Vector]) -> list[Vector]:
    antinode_locations = []
    for i, location_1 in enumerate(antenna_locations[:-1]):
        for location_2 in antenna_locations[i + 1 :]:
            relative_vector = location_1 - location_2
            antinode_locations += [
                location_1 + relative_vector,
                location_2 - relative_vector,
            ]
    return antinode_locations


def task_1(filepath: str = "input/8.txt") -> int:
    bottom_corner, antennae_locations = prepare_input(filepath)
    all_antinode_locations = []
    for _, locations in antennae_locations.items():
        all_antinode_locations += [
            location
            for location in find_antinodes(locations)
            if location not in all_antinode_locations
            and location.is_enclosed_by(Vector(0, 0), bottom_corner)
        ]
    return len(all_antinode_locations)
