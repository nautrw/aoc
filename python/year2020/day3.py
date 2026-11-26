import math
from utils import Day, run


class Day3(Day):
    def parse(self, raw: str):
        result = raw.strip().splitlines()
        return result, len(result[0])

    def part1(self, parsed):
        trees = 0

        # note: y component of slope is 1 so we can ignore it bc. we iter.
        # through the lines 1 by 1
        x_pos = 0

        for line in parsed[0]:
            if line[x_pos % parsed[1]] == "#":
                trees += 1

            x_pos += 3

        return trees

    def part2(self, parsed):
        slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
        trees_per_slope = []

        for slope in slopes:
            trees = 0

            delta_x, delta_y = slope

            x_pos = 0
           
            for i in range(0, len(parsed[0]), delta_y):
                row = parsed[0][i]
                if row[x_pos % parsed[1]] == "#":
                    trees += 1

                x_pos += delta_x

            trees_per_slope.append(trees)

        return math.prod(trees_per_slope)


if __name__ == "__main__":
    run(Day3)
