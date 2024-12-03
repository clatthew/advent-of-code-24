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


def extract_muls_2(corrupted_data):
    pattern = compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    return pattern.findall(corrupted_data)


def task_2(corrupted_data=get_input_string()):
    mul = compile(r"mul\((\d+),(\d+)\)")
    do = compile(r"do\(\)")
    dont = compile(r"don't\(\)")
    doing = True
    total = 0
    for instruction in extract_muls_2(corrupted_data):
        if do.match(instruction):
            doing = True
        elif dont.match(instruction):
            doing = False
        if not doing:
            continue
        if mul.match(instruction):
            a, b = mul.findall(instruction)[0]
            total += int(a) * int(b)
    return total
