import shutil
from argparse import ArgumentParser, Namespace
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

SRC_DIR = Path("src")
TESTS_DIR = Path("tests")
DAY_TEMPLATE_PATH = Path("templates/day.py")
TEST_TEMPLATE_PATH = Path("templates/examples.json")
EST = ZoneInfo("America/New_York")


def get_current_date_est() -> datetime:
    return datetime.now(EST)


def get_aoc_status() -> bool:
    now = get_current_date_est()
    dec_1 = datetime(now.year, 12, 1, 0, 0, 0, tzinfo=EST)
    dec_26 = datetime(now.year, 12, 26, 0, 0, 0, tzinfo=EST)
    return dec_1 <= now < dec_26


def parse_args() -> Namespace:
    now = get_current_date_est()
    year, day = now.year, now.day
    is_aoc_active = get_aoc_status()

    parser = ArgumentParser(description="Advent of Code Generator")
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        choices=range(2015, year + 1),
        default=year,
        help="Year of the puzzles (default: current year)",
        metavar=f"{{2015-{year}}}",
    )
    parser.add_argument(
        "-d",
        "--days",
        type=int,
        choices=range(1, 26),
        nargs="+",
        default=day if is_aoc_active else -1,
        help="Day(s) of the puzzles. Provide a single day (e.g., '-d 5') or a range (e.g., '-d 1 5'). (default: current day, if AOC is active)",  # noqa: E501
        metavar="{1-25}",
    )

    args = parser.parse_args()
    if args.days == -1:
        parser.error(
            "The -d/--days flag is required outside the Advent of Code active period (Dec 1 - Dec 25). "  # noqa: E501
            "Please specify a day using '-d DAY' or a range with '-d START END'.",
        )
    if len(args.days) > 2:
        parser.error(
            "The -d/--days flag accepts only 1 or 2 values (a single day or a range).",
        )

    return args


def create_file(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content)
        print(f"Created: {path}")
    else:
        print(f"Skipped (already exists): {path}")


def generate(year: int, days: list[int]) -> None:
    year_src_dir = SRC_DIR / str(year)
    year_tests_dir = TESTS_DIR / str(year)
    year_src_dir.mkdir(parents=True, exist_ok=True)
    year_tests_dir.mkdir(parents=True, exist_ok=True)

    start_day, end_day = (days[0], days[-1])
    for day in range(start_day, end_day + 1):
        day_file = year_src_dir / f"d{day:02}.py"
        test_file = year_tests_dir / f"d{day:02}.json"

        if not day_file.exists():
            shutil.copy(DAY_TEMPLATE_PATH, day_file)
            print(f"Created: {day_file}")
        else:
            print(f"Skipped: {day_file} (already exists)")

        if not test_file.exists():
            shutil.copy(TEST_TEMPLATE_PATH, test_file)
            print(f"Created: {test_file}")
        else:
            print(f"Skipped: {test_file} (already exists)")


def main() -> None:
    args = parse_args()
    year, days = args.year, args.days

    generate(year, days=days)


if __name__ == "__main__":
    main()
