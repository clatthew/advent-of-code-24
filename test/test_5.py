from pytest import mark
from src.day_5 import check_update, tasks, get_badly_ordered_updates, fix_update


class Testcheck_update:
    @mark.it("returns middle page number of valid update")
    def test_1(self):
        test_update = [75, 47, 61, 53, 29]
        test_conditions = {
            53: [47, 75, 61, 97],
            13: [97, 61, 29, 47, 75, 53],
            61: [97, 47, 75],
            47: [97, 75],
            29: [75, 97, 53, 61, 47],
            75: [97],
        }
        result = check_update(test_update, test_conditions)
        expected = 61
        assert result == expected

    @mark.it("returns 0 for invalid update")
    def test_2(self):
        test_update = [75, 97, 47, 61, 53]
        test_conditions = {
            53: [47, 75, 61, 97],
            13: [97, 61, 29, 47, 75, 53],
            61: [97, 47, 75],
            47: [97, 75],
            29: [75, 97, 53, 61, 47],
            75: [97],
        }
        result = check_update(test_update, test_conditions)
        expected = 0
        assert result == expected


class Testfix_update:
    @mark.it("Returns original middle number for update which is already valid")
    def test_1(self):
        test_update = [75, 47, 61, 53, 29]
        test_conditions = {
            53: [47, 75, 61, 97],
            13: [97, 61, 29, 47, 75, 53],
            61: [97, 47, 75],
            47: [97, 75],
            29: [75, 97, 53, 61, 47],
            75: [97],
        }
        result = fix_update(test_update, test_conditions)
        expected = 61
        assert result == expected

    @mark.it("Returns middle number after fixing an update")
    def test_2(self):
        test_update = [61, 13, 29]
        test_conditions = {
            53: [47, 75, 61, 97],
            13: [97, 61, 29, 47, 75, 53],
            61: [97, 47, 75],
            47: [97, 75],
            29: [75, 97, 53, 61, 47],
            75: [97],
        }
        result = fix_update(test_update, test_conditions)
        expected = 29
        assert result == expected


@mark.it("Solution to task 1 returns the correct answer")
def test_1():
    assert tasks() == 5948


@mark.it("Solution to task 2 returns the correct answer")
def test_2():
    assert tasks(get_badly_ordered_updates, fix_update) == 3062
