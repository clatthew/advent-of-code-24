from pytest import mark, fixture
from src.day_12 import Solution
from src.day_4 import get_matrix, Vector
from copy import deepcopy
from pprint import pprint


class Testregion_containing:
    @mark.it("Identifies region when the map contains a single plot type")
    def test_1(self):
        test_map = [list("AAAA") for _ in range(4)]
        test_solution = Solution(deepcopy(test_map))
        result = [
            i.as_tuple for i in test_solution.region_containing(Vector(1, 1), test_map)
        ]
        expected = [
            (1, 1),
            (2, 1),
            (3, 1),
            (3, 2),
            (3, 3),
            (2, 3),
            (1, 3),
            (0, 3),
            (0, 2),
            (1, 2),
            (2, 2),
            (0, 1),
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
        ]
        assert result == expected


class Testfind_regions:
    @mark.it(
        "Produces a list of regions for a map with a single region, with the region containing the correct points"
    )
    def test_1(self):
        test_map = [list("AAAA") for _ in range(4)]
        test_solution = Solution(test_map)
        result = [i.as_tuple for i in test_solution.regions[0].plots]
        expected = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
            (2, 3),
            (1, 3),
            (0, 3),
            (0, 2),
            (1, 2),
            (2, 2),
            (2, 1),
            (1, 1),
            (0, 1),
        ]
        assert result == expected

    @mark.it("Produces a list of regions for for the first sample data")
    def test_2(self):
        test_solution = Solution(get_matrix("test/test_data/12_1.txt"))
        result = [[j.as_tuple for j in i.plots] for i in test_solution.regions]
        expected = [
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(0, 1), (1, 1), (1, 2), (0, 2)],
            [(2, 1), (2, 2), (3, 2), (3, 3)],
            [(3, 1)],
            [(0, 3), (1, 3), (2, 3)],
        ]
        assert result == expected

    @mark.it("Produces a list of regions for for the second sample data")
    def test_3(self):
        test_solution = Solution(get_matrix("test/test_data/12_2.txt"))
        result = [[j.as_tuple for j in i.plots] for i in test_solution.regions]
        expected = [
            [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (4, 1),
                (4, 2),
                (4, 3),
                (4, 4),
                (3, 4),
                (2, 4),
                (1, 4),
                (0, 4),
                (0, 3),
                (0, 2),
                (1, 2),
                (2, 2),
                (3, 2),
                (2, 3),
                (2, 1),
                (0, 1),
            ],
            [(1, 1)],
            [(3, 1)],
            [(1, 3)],
            [(3, 3)],
        ]
        assert result == expected


class Testperimiter:
    @mark.parametrize(
        "sample_data,expected",
        [
            (1, [10, 8, 10, 4, 8]),
            (2, [36, 4, 4, 4, 4]),
            (3, [18, 8, 28, 18, 20, 20, 4, 18, 22, 12, 8]),
        ],
    )
    @mark.it("calculates correct perimeters for sample data")
    def test_1(self, sample_data, expected):
        test_solution = Solution(get_matrix(f"test/test_data/12_{sample_data}.txt"))
        result = [i.perimeter for i in test_solution.regions]
        assert result == expected


@fixture
def solution():
    return Solution(get_matrix("input/12.txt"))


class Testtasks:
    @mark.parametrize("sample_data,expected", [(1, 140), (2, 772), (3, 1930)])
    @mark.it("correct solution to task 1 with sample data")
    def test_1(self, sample_data, expected):
        solution = Solution(get_matrix(f"test/test_data/12_{sample_data}.txt"))
        result = sum([region.cost_1 for region in solution.regions])
        assert result == expected

    @mark.skip
    @mark.it("correct solution to task 1")
    def test_2(self, solution):
        expected = 1464678
        result = sum([region.cost_1 for region in solution.regions])
        assert result == expected

    # @mark.skip
    @mark.parametrize("sample_data,expected", [(1, 80), (2, 436), (3, 1206)])
    @mark.it("correct solution to task 2 with sample data")
    def test_3(self, sample_data, expected):
        solution = Solution(get_matrix(f"test/test_data/12_{sample_data}.txt"))
        # print([[i.as_tuple for i in j.plots] for j in solution.regions])
        result = sum([region.cost_2 for region in solution.regions])
        assert result == expected

    @mark.skip
    @mark.it("correct solution to task 2")
    def test_4(self, solution):
        expected = 1464678
        result = sum([region.cost_2 for region in solution.regions])
        assert result == expected
