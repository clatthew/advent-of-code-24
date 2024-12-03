def read_input(day):
    with open(f"input/{day}.txt", "r") as f:
        for line in f:
            yield line.split()
