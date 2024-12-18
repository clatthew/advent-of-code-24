from src.day_4 import Vector
from src.day_6 import unit_vectors
from typing import Union
from copy import copy
from pprint import pprint


def construct_matrix(dim, val):
    return [[val for _ in range(dim)] for _ in range(dim)]


def construct_maze(
    filepath: str, len: int = 71, limit: int = 0, width=1, dot=".", wall="#"
) -> list[list[str]]:
    dot = dot * width
    wall = wall * width
    maze = [[dot for _ in range(len)] for _ in range(len)]
    walls = 0
    with open(filepath) as f:
        for i, line in enumerate(f):
            x, y = tuple([int(i) for i in line.split(",")])
            maze[y][x] = wall
            walls += 1
            if i + 1 == limit:
                return maze
    print(walls)
    return maze


def add_path(filepath, maze, width):
    with open(filepath) as f:
        for i, (line) in enumerate(f):
            x, y = tuple([int(i) for i in line.split(",")])
            # maze[y][x] = f"{i:03d}"
            maze[y][x] = "o"
    with open("maze_with_path.txt", "w") as f:
        for line in maze:
            f.write(" ".join(line) + "\n")


def navigate_maze(
    maze: list[list[str]],
    starting_pos: Vector = Vector(0, 0),
    goal_pos: Vector = Vector(70, 70),
    previously_visited: list[Vector] = [],
) -> Union[int, None]:
    # with open("start_pos.txt", "a+") as f:
    #     f.write(f"{starting_pos.as_tuple}\n")

    if starting_pos == goal_pos:
        # if len(previously_visited) == 22:
        print("reached")
        print([i.as_tuple for i in previously_visited])
        print(len(previously_visited))

        with open("steps.txt", "w") as f:
            for pos in previously_visited:
                f.write(f"{pos.x},{pos.y}\n")
        return 0
    if starting_pos.index(maze, True) != ".":
        # print(starting_pos)
        return None
    previously_visited.append(starting_pos)
    paths = []
    for _, direction in unit_vectors.items():
        next_step = starting_pos + direction
        if next_step in previously_visited or not next_step.is_inside_of(maze):
            continue
        try:
            steps_to_goal = navigate_maze(
                maze, next_step, goal_pos, copy(previously_visited)
            )
        except RecursionError:
            steps_to_goal = None
        if steps_to_goal is not None:
            paths.append(steps_to_goal + 1)
    if paths:
        return min(paths)
    return None


class Solution:
    def __init__(self, filepath, dim, limit):
        self.was_here = construct_matrix(dim, 0)
        self.maze = construct_maze(filepath, dim, limit, dot=0, wall=1)
        self.target = Vector(dim - 1, dim - 1)
        self.correct_path = construct_matrix(dim, 0)

    def recursive_solve(self, start_pos: Vector = Vector(0, 0)):
        if start_pos == self.target:
            return True
        if start_pos.index(self.maze) or start_pos.index(self.was_here):
            return False
        start_pos.set_value(self.was_here, 1)
        for _, direction in unit_vectors.items():
            next_step = start_pos + direction
            if next_step.index(self.maze, True) is None:
                continue
            if self.recursive_solve(next_step):
                start_pos.set_value(self.correct_path, 1)
                return True
        return False

    def get_no_steps(self):
        return sum([sum(row) for row in self.correct_path])


if __name__ == "__main__":
    # add_path("steps.txt", construct_maze("test/test_data/18.txt", 7, 12))
    # add_path("steps.txt", construct_maze("input/18.txt", limit=1024, width=1), 1)
    solution = Solution("test/test_data/18.txt", 7, 12)
    solution.recursive_solve()
    pprint(solution.correct_path)
    print(solution.get_no_steps())
    solution = Solution("input/18.txt", 71, 1024)
    solution.recursive_solve()
    pprint(solution.correct_path)
    print(solution.get_no_steps())
