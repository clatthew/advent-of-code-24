from typing import Union


def input_string(filepath: str):
    with open(filepath) as f:
        return f.read()


def data_chunks(data: str) -> list[int]:
    return [int(i) for i in data[::2]]


def empty_chunks(data: str) -> list[int]:
    return [int(i) for i in data[1::2]] + [0]


def uncompressed_rep(
    data: list[int], nested: bool = False
) -> list[int] | list[Union[list[int], int]]:
    uncompressed_data = []
    for i, (data_len, empty_len) in enumerate(
        zip(data_chunks(data), empty_chunks(data))
    ):
        next_data_chunk = [i] * data_len
        if nested:
            uncompressed_data.append(next_data_chunk)
            uncompressed_data.append(empty_len)
        else:
            next_empty_chunk = [None] * empty_len
            uncompressed_data += next_data_chunk + next_empty_chunk
    return uncompressed_data


def compressed_rep_1(uncompressed_data: list[int]) -> list[int]:
    compressed_data = []
    end_pointer = len(uncompressed_data) - 1
    for i, chunk in enumerate(uncompressed_data):
        if chunk is None:
            while uncompressed_data[end_pointer] is None:
                if i == end_pointer:
                    return compressed_data
                end_pointer -= 1
            compressed_data.append(uncompressed_data[end_pointer])
            end_pointer -= 1
        else:
            compressed_data.append(chunk)
            if i >= end_pointer:
                return compressed_data


def generate_checksum(data: list[int]) -> int:
    return sum([i * chunk for i, chunk in enumerate(data) if chunk is not None])


def task_1(filepath: str = "input/9.txt") -> int:
    data = input_string(filepath)
    uncompressed_data = uncompressed_rep(data)
    compressed_data = compressed_rep_1(uncompressed_data)
    return generate_checksum(compressed_data)


def find_gap_to_fit(
    chunk: list[int], uncompressed_data: list[Union[list[int], int]]
) -> int | None:
    for i, gap_size in enumerate(uncompressed_data):
        if isinstance(gap_size, int):
            if len(chunk) <= gap_size:
                return i
    return None


def merge_adjacents(
    uncompressed_data: list[Union[list[int], int]],
) -> list[Union[list[int], int]]:
    for i, (gap_1, gap_2) in enumerate(
        zip(uncompressed_data[:-1], uncompressed_data[1:])
    ):
        if isinstance(gap_1, int) and isinstance(gap_2, int):
            uncompressed_data[i] += gap_2
            uncompressed_data[i + 1] = 0
    return [i for i in uncompressed_data if i]


def make_optimisation(
    old_chunk_pos: int,
    candidate_chunk: list[int],
    uncompressed_data: list[Union[list[int], int]],
) -> list[Union[list[int], int]]:
    gap_pos = find_gap_to_fit(candidate_chunk, uncompressed_data)
    if gap_pos is None or gap_pos > old_chunk_pos:
        return uncompressed_data
    uncompressed_data[old_chunk_pos] = len(candidate_chunk)
    uncompressed_data.insert(gap_pos, candidate_chunk)
    uncompressed_data[gap_pos + 1] = uncompressed_data[gap_pos + 1] - len(
        candidate_chunk
    )
    while True:
        compressed_data = merge_adjacents(uncompressed_data)
        if compressed_data == merge_adjacents(compressed_data):
            return compressed_data


def compressed_rep_2(uncompressed_data: list[Union[list[int], int]]) -> list[int]:
    for backward_chunk in uncompressed_data[::-1]:
        if isinstance(backward_chunk, list):
            uncompressed_data = make_optimisation(
                uncompressed_data.index(backward_chunk),
                backward_chunk,
                uncompressed_data,
            )
    compressed_data = []
    for chunk in uncompressed_data:
        if isinstance(chunk, int):
            compressed_data += [0] * chunk
        else:
            compressed_data += chunk
    return compressed_data


def task_2(filepath: str = "input/9.txt") -> int:
    data = input_string(filepath)
    uncompressed_data = uncompressed_rep(data, True)
    compressed_data = compressed_rep_2(uncompressed_data)
    return generate_checksum(compressed_data)
