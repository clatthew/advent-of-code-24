def prepare_input(filepath: str = "input/7.txt") -> dict:
    numbers = {}
    with open(filepath) as f:
        for line in f:
            split_line = line.split(": ")
            numbers[int(split_line[0])] = [int(i) for i in split_line[1].split(" ")]
    return numbers


def rep(n: int, chunk_size: int, base: int) -> str:
    rep = []
    for exponent in range(chunk_size - 1, -1, -1):
        quotient, n = divmod(n, base**exponent)
        rep.append(quotient)
    return rep


def reps(length: int, base=2) -> list[str]:
    return [rep(i, length, base) for i in range(base**length)]


def combine(components: list[int], permutation: list[int]) -> int:
    result = components[0]
    for component, operator in zip(components[1:], permutation):
        match operator:
            case 0:
                result = result * component
            case 1:
                result += component
            case 2:
                result = int(f"{result}{component}")
    return result


def can_be_true(total: int, components: list[int], base: int) -> bool:
    for permutation in reps(len(components) - 1, base):
        if combine(components, permutation) == total:
            return True
    return False


def tasks(equations: dict = prepare_input(), base: int = 2) -> int:
    current_result = 0
    for total, components in equations.items():
        if can_be_true(total, components, base):
            current_result += total
    return current_result
