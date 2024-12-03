from re import compile


def get_input_string():
    with open("input/3.txt") as f:
        return f.read()


def extract_muls(corrupted_data):
    pattern = compile(r"mul\((\d+),(\d+)\)")
    return pattern.findall(corrupted_data)


def task_1(corrupted_data=get_input_string()):
    total = 0
    for a, b in extract_muls(corrupted_data):
        total += int(a) * int(b)
    return total
