import importlib
import sys
from argparse import ArgumentParser, Namespace
from datetime import datetime
from time import perf_counter
from types import ModuleType
from zoneinfo import ZoneInfo

from aocd import get_data, submit

from tests.test import run_tests


def get_current_date_est() -> tuple[int, int]:
    est = ZoneInfo("America/New_York")  # EST timezone
    now = datetime.now(est)
    return now.year, now.day


def parse_args() -> Namespace:
    year, day = get_current_date_est()

    parser = ArgumentParser(
        description="Advent of Code Runner",
    )
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        choices=range(2015, year + 1),
        default=year,
        help="Year of the puzzle (default: current year)",
        metavar=f"{{2015-{year}}}",
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        choices=range(1, 26),
        default=day,
        help="Day of the puzzle (default: current day)",
        metavar="{1-25}",
    )

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument(
        "-t",
        "--test",
        nargs="?",
        type=int,
        choices=[1, 2],
        const=0,
        help="Run tests on examples. Optionally, specify 1 or 2 for which part to test.",  # noqa: E501
    )
    action_group.add_argument(
        "-s",
        "--submit",
        nargs=1,
        type=int,
        choices=[1, 2],
        help="Submit your solution. Specify 1 or 2 for which part to submit.",
    )

    return parser.parse_args()


def load_solution(year: int, day: int) -> ModuleType:
    module_path = f"src.{year}.d{day:02}"
    try:
        return importlib.import_module(module_path)
    except ModuleNotFoundError:
        print(f"Solution file for year {year}, day {day} not found.")
        sys.exit(1)


def main() -> None:
    args = parse_args()
    year, day = args.year, args.day
    solution = load_solution(year, day)
    data = get_data(day=day, year=year)

    if args.test is not None:
        test_file_path = f"tests/{year}/d{day:02}.json"
        print(f"Testing Year {year}, Day {day}...")
        match args.test:
            case 0:
                run_tests(
                    test_file_path,
                    part=1,
                    parse_f=solution.parse,
                    part_f=solution.part1,
                )
                run_tests(
                    test_file_path,
                    part=2,
                    parse_f=solution.parse,
                    part_f=solution.part2,
                )
            case 1:
                run_tests(
                    test_file_path,
                    part=1,
                    parse_f=solution.parse,
                    part_f=solution.part1,
                )
            case 2:
                run_tests(
                    test_file_path,
                    part=2,
                    parse_f=solution.parse,
                    part_f=solution.part2,
                )
    elif args.submit:
        match args.submit[0]:
            case 1:
                print(f"Submitting Year {year}, Day {day}, Part 1...")
                parsed_data = solution.parse(data)
                output = solution.part1(parsed_data)
                submit(output, part="a", day=day, year=year, reopen=False)
            case 2:
                print(f"Submitting Year {year}, Day {day}, Part 2...")
                parsed_data = solution.parse(data)
                output = solution.part2(parsed_data)
                submit(output, part="b", day=day, year=year, reopen=False)
    else:
        start_parse = perf_counter()
        parsed_data = solution.parse(data)
        end_parse = perf_counter()

        start_part1 = perf_counter()
        part1_result = solution.part1(*parsed_data[1])
        end_part1 = perf_counter()
        print(
            f"Part 1:{"\n" if "\n" in str(part1_result) else " "}{part1_result} (Time: {(end_part1 - start_part1) + (end_parse - start_parse):.5f}s)",  # noqa: E501
        )

        start_part2 = perf_counter()
        part2_result = solution.part2(*parsed_data[2])
        end_part2 = perf_counter()
        print(
            f"Part 2:{"\n" if "\n" in str(part2_result) else " "}{part2_result} (Time: {(end_part2 - start_part2) + (end_parse - start_parse):.5f}s)",  # noqa: E501
        )


if __name__ == "__main__":
    main()
