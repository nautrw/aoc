from utils import Day, run


class Day2(Day):
    def parse(self, raw: str):
        result = []

        for line in raw.strip().splitlines():
            parts = line.split()

            nums = tuple(map(int, parts[0].split("-")))
            letter = parts[1][0]
            password = parts[2]

            result.append((nums, letter, password))

        return result

    def part1(self, parsed):
        valid = 0
        for parts in parsed:
            occurences = parts[-1].count(parts[-2])

            if parts[0][0] <= occurences <= parts[0][1]:
                valid += 1

        return valid

    def part2(self, parsed):
        valid = 0
        for parts in parsed:
            try:
                letter1 = parts[2][parts[0][0] - 1]
                letter2 = parts[2][parts[0][1] - 1]
            except IndexError:
                continue

            # print(letter1, letter1 == parts[1], letter2, letter2 == parts[1])
            if (letter1 == parts[1] and letter2 != parts[1]) or (
                letter2 == parts[1] and letter1 != parts[1]
            ):
                valid += 1

        return valid


if __name__ == "__main__":
    run(Day2)
