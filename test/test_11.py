from src.day_11 import Solution
from pytest import mark, fixture


@fixture
def solution():
    return Solution()


@fixture
def sample_solution():
    return Solution("test/test_data/11.txt")


class Test__init__:
    @mark.it("forms initial list of stones from file")
    def test_1(self, solution: Solution):
        result = solution.stones
        expected = [3028, 78, 973951, 5146801, 5, 0, 23533, 857]
        assert result == expected


class Testtasks:
    @mark.it("solution to task 1 using sample data")
    def test_1(self, sample_solution: Solution):
        result = sample_solution.task(25)
        expected = 55312
        assert result == expected

    @mark.it("solution to task 1")
    def test_2(self, solution: Solution):
        result = solution.task()
        expected = 198089
        assert result == expected

    @mark.it("solution to task 2")
    def test_3(self, solution: Solution):
        result = solution.task(75)
        expected = 236302670835517
        assert result == expected
