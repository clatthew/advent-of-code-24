def read_input(day: int):
    """split each line of a text file into a list and return a generator of these lists"""
    with open(f"input/{day}.txt", "r") as f:
        for line in f:
            yield line.split()
