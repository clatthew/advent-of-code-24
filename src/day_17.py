from math import log
from typing import Literal, Union


class Computer:
    def __init__(self, filepath: str = "input/17.txt"):
        self.registers = {}
        self.filepath = filepath
        self.load_input(filepath)
        self.pointer = 0
        self.output = []
        self.opcodes = {
            (0,): self.adv,
            (1,): self.bxl,
            (1, 0): self.bst,
            (1, 1): self.jnz,
            (1, 0, 0): self.bxc,
            (1, 0, 1): self.out,
            (1, 1, 0): self.bdv,
            (1, 1, 1): self.cdv,
        }

    def update_combo_operands(self):
        self.combo_operands = {
            (0,): (0,),
            (1,): (1,),
            (1, 0): (1, 0),
            (1, 1): (1, 1),
            (1, 0, 0): self.registers["A"],
            (1, 0, 1): self.registers["B"],
            (1, 1, 0): self.registers["C"],
        }

    def load_input(self, filepath: str):
        with open(filepath) as f:
            text = f.read().split("\n\n")
        registers = text[0].split("\n")
        for i, register in enumerate(["A", "B", "C"]):
            self.registers[register] = binary_rep(
                int(registers[i][registers[i].index(":") + 2 :])
            )
        self.program = [int(i) for i in text[1][text[1].index(":") + 2 :].split(",")]

    def run_program(self):
        while self.pointer < len(self.program):
            self.update_combo_operands()
            opcode = binary_rep(self.program[self.pointer])
            operand = binary_rep(self.program[self.pointer + 1])
            try:
                self.opcodes[opcode](operand)
            except TypeError as t:
                print(f"{opcode=} {operand=} {self.registers=}")
                raise Exception
            self.pointer += 2
        return ",".join([str(i) for i in self.output])

    def adv(self, combo_operand: tuple[Literal[0, 1]]):
        """
        performs division.
        numerator: value in the A register
        denominator: 2 to the power of the combo operand
        result is truncated to an integer and written to register A.
        """
        literal_operand = self.combo_operands[combo_operand]
        self.registers["A"] = self.registers["A"][: -decimal_rep(literal_operand)]

    def bdv(self, combo_operand: tuple[Literal[0, 1]]):
        """
        performs division.
        numerator: value in the A register
        denominator: 2 to the power of the combo operand
        result is truncated to an integer and written to register B.
        """
        literal_operand = self.combo_operands[combo_operand]
        self.registers["B"] = self.registers["A"][: -decimal_rep(literal_operand)]

    def cdv(self, combo_operand: tuple[Literal[0, 1]]):
        """
        performs division.
        numerator: value in the A register
        denominator: 2 to the power of the combo operand
        result is truncated to an integer and written to register C.
        """
        literal_operand = self.combo_operands[combo_operand]
        self.registers["C"] = self.registers["A"][: -decimal_rep(literal_operand)]

    def bxl(self, literal_operand: tuple[Literal[0, 1]]):
        """
        performs bitwise XOR between the value in the B register and the literal operand.
        result is written to register B.
        """
        self.registers["B"] = bitwise_xor(self.registers["B"], literal_operand)

    def bst(self, combo_operand: tuple[Literal[0, 1]]):
        """
        calculates the value of the combo operand mod 8.
        result is written to register B.
        """
        literal_operand = self.combo_operands[combo_operand]
        self.registers["B"] = literal_operand[-3:]

    def jnz(self, literal_operand: tuple[Literal[0, 1]]):
        """
        does nothing if register A is 0.
        otherwise jumps the pointer to the value of the literal operand.
        """
        if not self.registers["A"]:
            return
        self.pointer = decimal_rep(literal_operand) - 2

    def bxc(self, _: tuple[Literal[0, 1]]):
        """
        calculate the bitwise XOR of register B and register C.
        result is written to register B.
        """
        self.registers["B"] = bitwise_xor(self.registers["B"], self.registers["C"])

    def out(self, combo_operand: tuple[Literal[0, 1]]):
        """
        adds the value of combo operand modulo 8 to the output
        """
        literal_operand = self.combo_operands[combo_operand]
        self.output.append(decimal_rep(literal_operand[-3:]))


def produce_copy(filepath: str = "input/17.txt"):
    i = 117440
    while True:
        if not i % 1000:
            print(i)
        computer = Computer(filepath)
        computer.registers["A"] = i
        program_string = ",".join([str(i) for i in computer.program])
        if computer.run_program() == program_string:
            return i
        i += 1


def binary_rep(n: int) -> Union[tuple[Literal[0, 1]], list[Literal[0, 1]]]:
    if not n:
        return (0,)
    rep = []
    magnitude = int(log(n, 2)) + 1
    for exponent in range(magnitude - 1, -1, -1):
        quotient, n = divmod(n, 2**exponent)
        rep.append(quotient)
    return tuple(rep)


def decimal_rep(n: tuple[Literal[0, 1]]) -> int:
    return sum([2**i * val for i, val in enumerate(n[::-1])])


def bitwise_xor(num1: int, num2: int) -> int:
    # bin1 = binary_rep(num1, True)
    # bin2 = binary_rep(num2, True)
    bin1 = list(num1)
    bin2 = list(num2)
    print(f"{bin1=} {bin2=}")
    len_diff = len(bin1) - len(bin2)
    if len_diff > 0:
        bin2 = [0 for _ in range(len_diff)] + bin2
    elif len_diff < 0:
        bin1 = [0 for _ in range(-len_diff)] + bin1
    print(f"{bin1=} {bin2=}")
    result = [(i - j) ** 2 for i, j in zip(bin1, bin2)]
    print(f"{num1=} {num2=} {result=}")
    # return decimal_rep(result)
    return tuple(result)
