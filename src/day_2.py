from src.read_input import read_input


def get_line_lists():
    yield from [[int(j) for j in i] for i in read_input(2)]


def is_safe(report: list[int], min_jump: int = 1, max_jump: int = 3) -> bool:
    ascending = report[0] < report[1]
    for i, j in zip(report[:-1], report[1:]):
        if ascending:
            if not i + min_jump <= j <= i + max_jump:
                return False
        else:
            if not i - max_jump <= j <= i - min_jump:
                return False
    return True


def count_safe_reports(safety_func=is_safe):
    report_gen = get_line_lists()
    return sum([safety_func(report) for report in report_gen])


def is_safe_2(report: list):
    for i, _ in enumerate(report):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


if __name__ == "__main__":
    print(count_safe_reports(is_safe_2))
