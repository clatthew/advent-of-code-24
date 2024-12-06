from src.day_6 import (
    task_1,
    get_start_pos,
    task_2,
    get_next_position,
    Vector,
    get_matrix,
)
from pytest import mark


class Testget_start_pos:
    @mark.it("Finds the guard's start position")
    def test_1(self):
        expected = Vector(95, 67)
        result = get_start_pos(get_matrix("input/6.txt"))
        assert result == expected


class Testget_next_position:
    @mark.it("Returns the next step of the guard")
    def test_1(self):
        test_data = {
            "map": [list("..#."), list("...."), list("#...."), list("....")],
            "current_position": Vector(0, 3),
            "current_direction": 3,
        }
        expected = Vector(1, 3)
        result, _ = get_next_position(**test_data)
        assert result == expected


class Testtasks:
    @mark.it("Solution to task 1 returns the correct answer")
    def test_3(self):
        assert task_1() == 5269

    @mark.skip
    @mark.it("Solution to task 2 returns the correct answer")
    def test_4(self):
        assert task_2()
