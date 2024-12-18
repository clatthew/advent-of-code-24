from re import compile


class System:
    def __init__(self, t: int, u: int, v: int, w: int, x: int, y: int, offset: int = 0):
        """
        Solve a system of simultaneous equations in (a, b) in the form
        - ta + ub = v
        - wa + xb = y

        where a, b are integers.
        """
        self.t = t
        self.u = u
        self.v = v + offset
        self.w = w
        self.x = x
        self.y = y + offset
        self.a = self.get_a()
        self.b = self.get_b()

    def get_a(self) -> int:
        float_division = (self.v * self.x - self.u * self.y) / (
            self.x * self.t - self.w * self.u
        )
        int_division = (self.v * self.x - self.u * self.y) // (
            self.x * self.t - self.w * self.u
        )
        if float_division == int_division:
            return int_division
        return None

    def get_b(self) -> int:
        if not self.a:
            return None
        return (self.y - self.w * self.a) // self.x

    @property
    def price(self) -> int:
        if self.a and self.b:
            return 3 * self.a + self.b
        return 0


def task(filepath: str = "input/13.txt", offset: int = 0) -> int:
    with open(filepath) as f:
        data = f.read()
    machines = data.split("\n\n")
    regex_pattern = compile(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    )
    tokens = 0
    for machine in machines:
        match = regex_pattern.match(machine)
        parameters = {
            "t": int(match.group(1)),
            "u": int(match.group(3)),
            "w": int(match.group(2)),
            "x": int(match.group(4)),
            "v": int(match.group(5)),
            "y": int(match.group(6)),
            "offset": offset,
        }
        tokens += System(**parameters).price
    return tokens


if __name__ == "__main__":
    print(f"Task 1: {task()}")
    print(f"Task 2: {task(offset=10000000000000)}")
