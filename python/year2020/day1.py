import itertools
import math

from utils import Day, run


def solve(nums, size: int = 2) -> int:
    return next(
        math.prod(pair)
        for pair in itertools.combinations(nums, size)
        if sum(pair) == 2020
    )


class Day1(Day):
    def parse(self, raw: str):
        return tuple(map(int, raw.strip().splitlines()))

    def part1(self, parsed):
        return solve(parsed)

    def part2(self, parsed):
        return solve(parsed, 3)


if __name__ == "__main__":
    run(Day1)
