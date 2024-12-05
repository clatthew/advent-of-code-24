def file_generator(filepath: str):
    with open(filepath) as f:
        yield from f


def add_to_dict(dict: dict, key, val):
    if key not in dict:
        dict[key] = [val]
    else:
        dict[key].append(val)


def extract_input(filepath: str = "input/5.txt"):
    input = file_generator(filepath)
    conditions = {}
    updates = []
    for line in input:
        if "|" in line:
            nums = [int(i) for i in line.split("|")]
            add_to_dict(conditions, nums[1], nums[0])
        elif "," in line:
            updates.append([int(page) for page in line.split(",")])
    return conditions, updates


def get_badly_ordered_updates():
    conditions, updates = extract_input()
    badly_ordered_updates = []
    for update in updates:
        if not check_update(update, conditions):
            badly_ordered_updates.append(update)
    return conditions, badly_ordered_updates


def get_check_update_fail_return_val(
    rearrange: bool, update: list, i: int, condition: int
):
    if rearrange:
        update.remove(condition)
        update.insert(i, condition)
        return update
    else:
        return 0


def get_middle_val(update: list):
    return update[int(len(update) / 2)]


def check_update(update: list, conditions: dict, rearrange: bool = False):
    for i, page in enumerate(update):
        for condition in conditions[page]:
            if condition in update and condition not in update[:i]:
                return get_check_update_fail_return_val(rearrange, update, i, condition)
    return get_middle_val(update)


def fix_update(update: list, conditions: dict):
    while not check_update(update, conditions):
        update = check_update(update, conditions, True)
    return get_middle_val(update)


def tasks(input_func=extract_input, score_func=check_update) -> int:
    conditions, updates = input_func()
    total = 0
    for update in updates:
        total += score_func(update, conditions)
    return total
