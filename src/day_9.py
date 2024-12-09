def input_string(filepath: str):
    with open(filepath) as f:
        return f.read()


def data_chunks(data: str) -> list[int]:
    return [int(i) for i in data[::2]]


def empty_chunks(data: str) -> list[int]:
    return [int(i) for i in data[1::2]] + [0]


def uncompressed_rep(data: list[int]) -> str:
    uncompressed_data = []
    for i, (data_len, empty_len) in enumerate(
        zip(data_chunks(data), empty_chunks(data))
    ):
        uncompressed_data += [i] * data_len
        uncompressed_data += [None] * empty_len
    return uncompressed_data


def compressed_rep(uncompressed_data: str) -> str:
    compressed_data = []
    end_pointer = len(uncompressed_data) - 1
    for i, chunk in enumerate(uncompressed_data):
        if i >= end_pointer:
            return compressed_data
        if chunk is None:
            while uncompressed_data[end_pointer] is None:
                end_pointer -= 1
                if i == end_pointer:
                    return compressed_data
            compressed_data.append(uncompressed_data[end_pointer])
            end_pointer -= 1
        else:
            compressed_data.append(chunk)


def generate_checksum(data: list[int]) -> int:
    return sum([i * chunk for i, chunk in enumerate(data)])


def task_1(filepath="input/9.txt") -> int:
    data = input_string(filepath)
    uncompressed_data = uncompressed_rep(data)
    with open("test/test_data/9_uncompressed.txt", "w") as f:
        f.write("".join([str(i) for i in uncompressed_data]))
    compressed_data = compressed_rep(uncompressed_data)
    return generate_checksum(compressed_data)
