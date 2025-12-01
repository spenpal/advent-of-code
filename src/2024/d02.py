from itertools import combinations


def parse(data: str) -> dict[int, tuple]:
    data = [tuple(map(int, line.split())) for line in data.strip().splitlines()]
    return {1: (data,), 2: (data,)}


def is_valid_report(report: tuple[int, ...]) -> bool:
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    return (all(diff < 0 for diff in diffs) or all(diff > 0 for diff in diffs)) and max(map(abs, diffs)) <= 3


def part1(reports: list[tuple[int, ...]]) -> int:
    return sum(is_valid_report(report) for report in reports)


def part2(reports: list[tuple[int, ...]]) -> int:
    total = 0
    for report in reports:
        if is_valid_report(report):
            total += 1
        else:
            report_combos = combinations(report, len(report) - 1)
            total += any(is_valid_report(report_combo) for report_combo in report_combos)
    return total
