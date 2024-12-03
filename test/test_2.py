from pytest import mark
from src.day_2 import count_safe_reports, is_safe


class Testis_safe:
    @mark.it("returns true for a safe increasing report")
    def test_1(self):
        test_data = [1, 3, 6, 7, 9]
        assert is_safe(test_data)

    @mark.it("returns true for a safe decreasing report")
    def test_2(self):
        test_data = [7, 6, 4, 2, 1]
        assert is_safe(test_data)

    @mark.it("returns false for unsafe increasing reports")
    def test_3(self):
        assert not is_safe([1, 2, 7, 8, 9])
        assert not is_safe([43, 46, 49, 52, 54, 58])

    @mark.it("returns false for an usafe decreasing report")
    def test_4(self):
        test_data = [9, 7, 6, 2, 1]
        assert not is_safe(test_data)

    @mark.it("returns false for a report containing identical consecutive numbers")
    def test_5(self):
        test_data = [8, 6, 4, 4, 1]
        assert not is_safe(test_data)


class Testpuzzles:
    def test_1(self):
        assert count_safe_reports() == 213
