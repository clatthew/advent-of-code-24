from pytest import mark
from src.day_7 import prepare_input, tasks, reps


class Testprepare_input:
    @mark.it("forms dict from file")
    def test_1(self):
        result = prepare_input("test/test_data/7.txt")
        expected = {
            190: [10, 19],
            3267: [81, 40, 27],
            83: [17, 5],
            156: [15, 6],
            7290: [6, 8, 6, 15],
            161011: [16, 10, 13],
            192: [17, 8, 14],
            21037: [9, 7, 18, 13],
            292: [11, 6, 16, 20],
        }
        assert result == expected

    @mark.it("includes all lines of text file")
    def test_2(self):
        assert len(prepare_input()) == 850


class Testreps:
    @mark.it("binary reps have the correct lengths")
    def test_1(self):
        for i in range(10):
            assert len(reps(i)) == 2**i

    @mark.it("all binary reps of length 4 are present")
    def test_2(self):
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
            [1, 1, 1, 1],
        ]
        result = reps(4)
        assert result == expected

    @mark.it("ternary reps have the correct lengths")
    def test_3(self):
        for i in range(10):
            assert len(reps(i, 3)) == 3**i

    @mark.it("all ternary reps of length 3 are present")
    def test_4(self):
        expected = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 2],
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 2],
            [0, 2, 0],
            [0, 2, 1],
            [0, 2, 2],
            [1, 0, 0],
            [1, 0, 1],
            [1, 0, 2],
            [1, 1, 0],
            [1, 1, 1],
            [1, 1, 2],
            [1, 2, 0],
            [1, 2, 1],
            [1, 2, 2],
            [2, 0, 0],
            [2, 0, 1],
            [2, 0, 2],
            [2, 1, 0],
            [2, 1, 1],
            [2, 1, 2],
            [2, 2, 0],
            [2, 2, 1],
            [2, 2, 2],
        ]
        result = reps(3, 3)
        assert result == expected


class Testtasks:
    @mark.it("task_1 returns correct solution for test data")
    def test_0(self):
        result = tasks(prepare_input("test/test_data/7.txt"))
        expected = 3749
        assert result == expected

    @mark.it("Solution to task 1 returns the correct answer")
    def test_1(self):
        result = tasks()
        expected = 1620690235709
        assert result == expected

    @mark.it("Solution to task 2 returns the correct answer")
    def test_2(self):
        assert tasks(base=3) == 145397611075341
