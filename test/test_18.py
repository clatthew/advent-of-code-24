from src.day_18 import construct_maze, navigate_maze
from src.day_4 import Vector
from pytest import mark, fixture


@fixture
def test_maze():
    return construct_maze("test/test_data/18.txt", 7, 12)


class Testconstruct_maze:
    @mark.it("constructs the maze with first 12 bytes in place with test data ")
    def test_1(self, test_maze):
        expected = [
            [".", ".", ".", "#", ".", ".", "."],
            [".", ".", "#", ".", ".", "#", "."],
            [".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", "#", ".", ".", "#"],
            [".", ".", "#", ".", ".", "#", "."],
            [".", "#", ".", ".", "#", ".", "."],
            ["#", ".", "#", ".", ".", ".", "."],
        ]
        result = test_maze
        assert result == expected

    @mark.it("constructs the maze with all bytes in place for test data")
    def test_2(self):
        expected = [
            [".", "#", "#", "#", ".", ".", "."],
            [".", "#", "#", ".", ".", "#", "#"],
            [".", "#", ".", ".", "#", ".", "."],
            [".", ".", ".", "#", ".", ".", "#"],
            ["#", "#", "#", ".", ".", "#", "#"],
            ["#", "#", "#", ".", "#", "#", "#"],
            ["#", "#", "#", ".", ".", ".", "."],
        ]
        result = construct_maze("test/test_data/18.txt", 7)
        assert result == expected


class Testnavigate_maze:
    # @mark.skip
    @mark.it("finds the smallest number of steps to navigate maze from test data")
    def test_1(self, test_maze):
        with open("maze.txt", "w") as f:
            for line in test_maze:
                f.write("".join(line) + "\n")
        expected = 22
        result = navigate_maze(test_maze, goal_pos=Vector(6, 6))
        assert result == expected

    @mark.skip
    @mark.it("finds the smallest number of steps to navigate maze with task input")
    def test_2(self):
        maze = construct_maze("input/18.txt", 71, 1024)
        with open("maze.txt", "w") as f:
            for line in maze:
                f.write(" ".join(line) + "\n")
        expected = 22
        result = navigate_maze(maze, starting_pos=Vector(41, 25))
        assert result == expected
