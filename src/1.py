def read_input(filepath="input/1.txt"):
    with open(filepath, "r") as f:
        for line in f:
            yield line.split()


def get_lists():
    lines = [line for line in read_input()]
    l_list = sorted(int(line[0]) for line in lines)
    r_list = sorted(int(line[1]) for line in lines)
    return l_list, r_list


def compare_lists(l_list, r_list):
    return sum(abs(a - b) for a, b in zip(l_list, r_list))


if __name__ == "__main__":
    print(compare_lists(*get_lists()))
