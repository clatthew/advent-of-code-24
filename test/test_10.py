from pytest import mark, fixture
from src.day_10 import Solution


@fixture
def solution():
    return Solution()


@fixture
def sample_solution():
    return Solution("test/test_data/10.txt")


class Testtasks:
    @mark.it("correct solution to task 1 with sample data")
    def test_0(self, sample_solution: Solution):
        expected = 36
        result = sample_solution.task()
        assert result == expected

    @mark.it("correct solution to task 1")
    def test_1(self, solution: Solution):
        expected = 698
        result = solution.task()
        assert result == expected

    @mark.it("correct solution to task 2 with sample data")
    def test_2(self, sample_solution: Solution):
        expected = 81
        result = sample_solution.task(2)
        assert result == expected

    @mark.it("correct solution to task 2")
    def test_3(self, solution: Solution):
        expected = 1436
        result = solution.task(2)
        assert result == expected
