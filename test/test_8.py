from pytest import mark
from src.day_8 import prepare_input, find_antinodes, tasks, antinodes_of_pair_1
from src.day_4 import Vector


class Testprepare_input:
    @mark.it("creates a dictionary of antenna location vectors")
    def test_1(self):
        expected = {
            "0": [(8, 1), (5, 2), (7, 3), (4, 4)],
            "A": [(6, 5), (8, 8), (9, 9)],
        }
        bottom_corner, antennae = prepare_input("test/test_data/8.txt")
        result_antennae = {
            antenna: [i.as_tuple for i in locations]
            for antenna, locations in antennae.items()
        }
        assert result_antennae == expected
        assert bottom_corner == Vector(11, 11)


class Testfind_antinodes:
    @mark.it(
        "returns a list of antinodes given a list of antenna locations using pair function 1"
    )
    def test_1(self):
        test_antennae_locations = [
            Vector(*location) for location in [(6, 5), (8, 8), (9, 9)]
        ]
        expected = [(4, 2), (10, 11), (3, 1), (7, 7), (10, 10)]
        result = [
            i.as_tuple
            for i in find_antinodes(
                test_antennae_locations, antinodes_of_pair_1, Vector(11, 11)
            )
        ]
        assert result == expected


class Testtasks:
    @mark.it("correct solution to task 1")
    def test_1(self):
        expected = 379
        result = tasks()
        assert result == expected

    @mark.it("correct solution to task 2 using test data")
    def test_2(self):
        expected = 34
        result = tasks("test/test_data/8.txt", 2)
        assert result == expected

    @mark.it("correct solution to task 2")
    def test_3(self):
        expected = 1339
        result = tasks(task=2)
        assert result == expected
