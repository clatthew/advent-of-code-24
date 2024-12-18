from pytest import mark, fixture
from src.day_17 import Computer, decimal_rep, binary_rep, bitwise_xor, produce_copy


@fixture
def computer():
    return Computer()


@fixture
def test_computer():
    return Computer("test/test_data/17.txt")


class Test_init__:
    @mark.it("loads the content of the registers")
    def test_1(self, test_computer: Computer):
        expected = {"A": 729, "B": 0, "C": 0}
        result = test_computer.registers
        assert result == expected

    @mark.it("loads the program")
    def test_2(self, test_computer: Computer):
        expected = [0, 1, 5, 4, 3, 0]
        result = test_computer.program
        assert result == expected


class Testdecimal_rep:
    @mark.parametrize("binary,expected", [([0, 1, 0], 2), ([1, 0, 1, 0], 10)])
    @mark.it("correct decimal representation of binary numbers")
    def test_1(self, binary: list[bool], expected: int):
        result = decimal_rep(binary)
        assert result == expected


class Testbinary_rep:
    @mark.parametrize("decimal,expected", [(2, [1, 0]), (10, [1, 0, 1, 0])])
    @mark.it("correct binary representation of decimal numbers")
    def test_1(self, decimal: int, expected: list[bool]):
        result = binary_rep(decimal)
        assert result == expected


class Testbitwise_xor:
    @mark.it("correct bitwise xor for numbers of the same number of bits")
    def test_1(self):
        num1 = 5
        num2 = 7
        expected = 2
        result = bitwise_xor(num1, num2)
        assert result == expected

    @mark.it("correct bitwise xor where num1 has more bits than num2")
    def test_2(self):
        num1 = 10
        num2 = 6
        expected = 12
        result = bitwise_xor(num1, num2)
        assert result == expected

    @mark.it("correct bitwise xor where num2 has more bits than num1")
    def test_3(self):
        num1 = 3
        num2 = 17
        expected = 18
        result = bitwise_xor(num1, num2)
        assert result == expected


class Testrun_program:
    @mark.it("correct steps taken for example 1")
    def test_2(self):
        computer = Computer("test/test_data/17_1.txt")
        computer.run_program()
        assert decimal_rep(computer.registers["B"]) == 1

    @mark.it("correct steps taken for example 2")
    def test_3(self):
        computer = Computer("test/test_data/17_2.txt")
        expected = "0,1,2"
        result = computer.run_program()
        assert result == expected

    @mark.it("correct steps taken for example 3")
    def test_4(self):
        computer = Computer("test/test_data/17_3.txt")
        expected = "4,2,5,6,7,7,7,7,3,1,0"
        result = computer.run_program()
        assert result == expected
        assert computer.registers["A"] == tuple()

    @mark.it("correct output for test data")
    def test_1(self, test_computer: Computer):
        expected = "4,6,3,5,6,3,5,2,1,0"
        result = test_computer.run_program()
        assert result == expected

    @mark.it("correct output for task 1")
    def test_5(self, computer: Computer):
        expected = "1,6,7,4,3,0,5,0,6"
        result = computer.run_program()
        assert result == expected

    @mark.skip
    @mark.it("correct output for task 2 with example data 4")
    def test_6(self):
        result = produce_copy("test/test_data/17_4.txt")
        expected = 117440
        assert result == expected

    @mark.skip
    @mark.it("correct output for task 2")
    def test_7(self):
        result = produce_copy()
        expected = 117440
        assert result == expected
