from pytest import mark
from src.day_9 import (
    input_string,
    data_chunks,
    empty_chunks,
    uncompressed_rep,
    task_1,
    compressed_rep_1,
    generate_checksum,
    task_2,
    find_gap_to_fit,
)


class Testdata_chunks:
    @mark.it("produces data and empty lengths for sample data")
    def test_1(self):
        expected = [2, 3, 1, 3, 2, 4, 4, 3, 4, 2]
        result = data_chunks(input_string("test/test_data/9.txt"))
        assert result == expected


class Testempty_chunks:
    @mark.it("produces data and empty lengths for sample data")
    def test_1(self):
        expected = [3, 3, 3, 1, 1, 1, 1, 1, 0, 0]
        result = empty_chunks(input_string("test/test_data/9.txt"))
        assert result == expected


class Testuncompressed_rep:
    @mark.it("produces uncompressed rep of sample data")
    def test_1(self):
        expected = [
            0,
            0,
            None,
            None,
            None,
            1,
            1,
            1,
            None,
            None,
            None,
            2,
            None,
            None,
            None,
            3,
            3,
            3,
            None,
            4,
            4,
            None,
            5,
            5,
            5,
            5,
            None,
            6,
            6,
            6,
            6,
            None,
            7,
            7,
            7,
            None,
            8,
            8,
            8,
            8,
            9,
            9,
        ]
        result = uncompressed_rep(input_string("test/test_data/9.txt"))
        assert result == expected

    @mark.it("produces uncompressed rep of sample data with nesting")
    def test_2(self):
        expected = [
            [0, 0],
            3,
            [1, 1, 1],
            3,
            [2],
            3,
            [3, 3, 3],
            1,
            [4, 4],
            1,
            [5, 5, 5, 5],
            1,
            [6, 6, 6, 6],
            1,
            [7, 7, 7],
            1,
            [8, 8, 8, 8],
            0,
            [9, 9],
            0,
        ]
        result = uncompressed_rep(input_string("test/test_data/9.txt"), True)
        assert result == expected


class Testcompressed_rep_1:
    @mark.it("produces compressed rep of sample data")
    def test_1(self):
        uncompressed_data = uncompressed_rep(input_string("test/test_data/9.txt"))
        expected = [
            0,
            0,
            9,
            9,
            8,
            1,
            1,
            1,
            8,
            8,
            8,
            2,
            7,
            7,
            7,
            3,
            3,
            3,
            6,
            4,
            4,
            6,
            5,
            5,
            5,
            5,
            6,
            6,
        ]
        result = compressed_rep_1(uncompressed_data)
        assert result == expected


class Testfind_gap_to_fit:
    def test_1(self):
        uncompressed_data = uncompressed_rep(input_string("test/test_data/9.txt"), True)
        expected = 1
        result = find_gap_to_fit([9, 9], uncompressed_data)
        assert result == expected


class Testgenerate_checksum:
    @mark.it("produces checksum of sample data")
    def test_1(self):
        compressed_data = compressed_rep_1(
            uncompressed_rep(input_string("test/test_data/9.txt"))
        )
        expected = 1928
        result = generate_checksum(compressed_data)
        assert result == expected


class Testtasks:
    @mark.it("correct answer to task 1")
    def test_2(self):
        expected = 6398608069280
        result = task_1()
        assert result == expected

    # @mark.skip
    @mark.it("correct answer to task 2 with sample data")
    def test_3(self):
        expected = 2858
        result = task_2("test/test_data/9.txt")
        assert result == expected

    @mark.it("correct answer to task 2")
    def test_4(self):
        expected = 6427437134372
        result = task_2()
        assert result == expected
