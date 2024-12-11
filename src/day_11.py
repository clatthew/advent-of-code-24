class Solution:
    def __init__(self, filepath: str = "input/11.txt"):
        with open(filepath) as f:
            self.stones = [int(i) for i in f.read().split(" ")]
        self.cache = {}

    def blink(self, stone: int) -> list[int]:
        new_stones = []
        stone_str = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(stone_str) % 2 == 0:
            midpoint = len(stone_str) // 2
            new_stones += [int(stone_str[:midpoint]), int(stone_str[midpoint:])]
        else:
            new_stones.append(2024 * stone)
        return new_stones

    def blink_single_stone(self, stone: int, blinks: int) -> int:
        if blinks == 1:
            return len(self.blink(stone))
        return self.blink_all_stones(self.blink(stone), blinks - 1)

    def blink_all_stones(self, stones: list[int] = [], blinks: int = 25) -> int:
        if not stones:
            stones = self.stones
        total_stones = 0
        for stone in stones:
            try:
                total_stones += self.cache[stone][blinks]
            except KeyError:
                result = self.blink_single_stone(stone, blinks)
                self.update_cache(stone, blinks, result)
                total_stones += result
        return total_stones

    def update_cache(self, stone: int, blinks: int, resulting_stones: int):
        if stone not in self.cache:
            self.cache[stone] = {blinks: resulting_stones}
        else:
            self.cache[stone][blinks] = resulting_stones
