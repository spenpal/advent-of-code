import importlib
import sys
import traceback
from argparse import ArgumentParser, Namespace
from datetime import datetime
from time import perf_counter
from types import ModuleType
from zoneinfo import ZoneInfo

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from aocd import get_data, submit

from tests.test import run_tests


def get_current_date_est() -> tuple[int, int]:
    est = ZoneInfo("America/New_York")  # EST timezone
    now = datetime.now(est)
    return now.year, now.day


def parse_args() -> Namespace:
    year, day = get_current_date_est()

    parser = ArgumentParser(description="Advent of Code Runner")
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
        help=(
            "Run tests on examples. Optionally, specify 1 or 2 for which part to test."
        ),
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
    except ModuleNotFoundError as e:
        print(f"An error occurred while importing {module_path}: {e}")
        print("Detailed traceback:")
        traceback.print_exc()
        sys.exit(1)


def run_test_mode(
    year: int,
    day: int,
    test_part: int,
    solution: ModuleType,
) -> None:
    test_file_path = f"tests/{year}/d{day:02}.json"
    print(f"Testing Year {year}, Day {day}...")
    match test_part:
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


def run_submit_mode(
    year: int,
    day: int,
    submit_part: int,
    solution: ModuleType,
    data: str,
) -> None:
    match submit_part:
        case 1:
            print(f"Submitting Year {year}, Day {day}, Part 1...")
            start_time = perf_counter()
            parsed_data = solution.parse(data)
            output = solution.part1(*parsed_data[1])
            end_time = perf_counter()
            elapsed_time = end_time - start_time
            submit(output, part="a", day=day, year=year, reopen=False)
            print(f"Time: {elapsed_time:.5f}s")
        case 2:
            print(f"Submitting Year {year}, Day {day}, Part 2...")
            start_time = perf_counter()
            parsed_data = solution.parse(data)
            output = solution.part2(*parsed_data[2])
            end_time = perf_counter()
            elapsed_time = end_time - start_time
            submit(output, part="b", day=day, year=year, reopen=False)
            print(f"Time: {elapsed_time:.5f}s")


def run_normal_mode(
    solution: ModuleType,
    data: str,
) -> None:
    start_parse = perf_counter()
    parsed_data = solution.parse(data)
    end_parse = perf_counter()

    start_part1 = perf_counter()
    part1_result = solution.part1(*parsed_data[1])
    end_part1 = perf_counter()
    part1_time = (end_part1 - start_part1) + (end_parse - start_parse)
    part1_sep = "\n" if "\n" in str(part1_result) else " "
    print(f"Part 1:{part1_sep}{part1_result} (Time: {part1_time:.5f}s)")

    start_part2 = perf_counter()
    part2_result = solution.part2(*parsed_data[2])
    end_part2 = perf_counter()
    part2_time = (end_part2 - start_part2) + (end_parse - start_parse)
    part2_sep = "\n" if "\n" in str(part2_result) else " "
    print(f"Part 2:{part2_sep}{part2_result} (Time: {part2_time:.5f}s)")


def main() -> None:
    args = parse_args()
    year, day = args.year, args.day
    solution = load_solution(year, day)
    data = get_data(day=day, year=year)

    if args.test is not None:
        run_test_mode(year, day, args.test, solution)
    elif args.submit:
        run_submit_mode(year, day, args.submit[0], solution, data)
    else:
        run_normal_mode(solution, data)


if __name__ == "__main__":
    main()
