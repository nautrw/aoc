import argparse
import sys
from abc import ABC, abstractmethod
from pathlib import Path

INPUTS_PATH = Path(__file__).resolve().parents[2] / "inputs"


class Day(ABC):
    @abstractmethod
    def parse(self, raw: str): ...

    @abstractmethod
    def part1(self, parsed): ...

    def part2(self, parsed):
        raise NotImplementedError


def module_file(day: type[Day]) -> Path:
    file = sys.modules[day.__module__].__file__
    assert file is not None
    return Path(file)


def default_input(day: type[Day]) -> Path:
    path = module_file(day)
    return INPUTS_PATH / path.parent.name / f"{path.stem}.txt"


def run(day: type[Day], argv: list[str] | None = None) -> None:
    path = module_file(day)
    parser = argparse.ArgumentParser(prog=f"python -m {path.parent.name}.{path.stem}")
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=default_input(day),
        help="puzzle input file (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    try:
        raw = args.input.read_text().rstrip()
    except OSError as e:
        parser.exit(1, f"failed to read {args.input}: {e}")

    solution = day()
    for i, part in enumerate((solution.part1, solution.part2)):
        try:
            answer = part(solution.parse(raw))
        except NotImplementedError:
            continue

        if answer is not None:
            print(f"Part {i+1}")
            print(answer)
            print()
