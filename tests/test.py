import json
from collections.abc import Callable
from pathlib import Path
from time import perf_counter


def run_tests(
    test_file_path: str,
    part: int,
    parse_f: Callable[[str], dict[int, tuple]],
    part_f: Callable,
) -> None:
    with Path(test_file_path).open() as file:
        test_cases = json.load(file)

    print("=" * 50)
    print(f"PART {part}")
    print("=" * 50)

    for i, test_case in enumerate(test_cases, start=1):
        example = test_case["example"]
        answer = test_case[f"part{part}"]

        if answer == "":
            continue

        start_time = perf_counter()
        parsed_example: dict[int, tuple] = parse_f(example)
        output = part_f(*parsed_example[part])
        end_time = perf_counter()

        if str(output) == str(answer):
            status = "PASSED"
            status_color = "\033[92m"  # Green
        else:
            status = "FAILED"
            status_color = "\033[91m"  # Red

        print(
            f"{status_color}#{i:02} - {status}\033[0m".ljust(35),
            f"Time: {(end_time - start_time):.5f}s".rjust(20),
        )

        if status == "FAILED":
            print(f"  └── Output:{'\n' if '\n' in str(output) else ' '}{output}")
            print(f"  └── Expected: {answer}")
