from pytest import mark
from src.day_4 import follow_direction, Vector, task_1, task_2


@mark.it(
    "Returns the correct string for the given direction when there are enough letters in that direction"
)
@mark.parametrize(
    "direction,expected",
    [
        (0, "AMAX"),
        (1, "AMXM"),
        (2, "ASAM"),
        (3, "ASMX"),
        (4, "AAXM"),
        (5, "ASMM"),
        (6, "AMXM"),
        (7, "AMXX"),
    ],
)
def test_1(direction, expected):
    test_input = {
        "matrix": [
            list("XXXMMSAMXXMASXASAMMSMMS"),
            list("AMSMMASAMXXXXAXMAXAAMSA"),
            list("MAAAMAXXASMMASASMMSSSXA"),
            list("XSMSMSSMXAAMAXMASMXMMMM"),
            list("XXSXXAAXSSSMSSXMMMAXMAS"),
            list("XMASMMSMMAAAXXXMASXMMMM"),
            list("SMAMXMAXXAMMMMMXAXAXSSS"),
            list("XMMSSSMSSMSAXAAMSSSMMAX"),
            list("MAXAXAAAXXSXXMXSAAAMMMM"),
        ],
        "start_point": Vector(10, 3),
        "direction": direction,
    }
    result = follow_direction(**test_input)
    assert result == expected


@mark.it(
    "Returns None when there are not enough letters in the given direction to make XMAS"
)
@mark.parametrize(
    "direction,expected",
    [
        (0, None),
        (1, None),
        (2, "MSAA"),
        (3, None),
        (4, None),
        (5, None),
        (6, None),
        (7, None),
    ],
)
def test_2(direction, expected):
    test_input = {
        "matrix": [
            list("AMSMM"),
            list("MAAAM"),
            list("XSMSM"),
            list("XXSXX"),
            list("XMASM"),
            list("SMAMX"),
        ],
        "start_point": Vector(2, 2),
        "direction": direction,
    }
    result = follow_direction(**test_input)
    assert result == expected


@mark.it("Solution to task 1 returns the correct answer")
def test_3():
    assert task_1() == 2344


@mark.it("Solution to task 2 returns the correct answer")
def test_4():
    assert task_2() == 1815
