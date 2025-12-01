import json
import os
import sys
from argparse import ArgumentParser, Namespace
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx
from aocd.models import Puzzle

EST = ZoneInfo("America/New_York")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "x-ai/grok-4.1-fast:free"


def get_current_date_est() -> tuple[int, int]:
    now = datetime.now(EST)
    return now.year, now.day


def get_puzzle_html(year: int, day: int) -> str:
    puzzle = Puzzle(year=year, day=day)
    return puzzle._get_prose()


def create_extraction_prompt(puzzle_html: str) -> str:
    return f"""You are extracting test examples from an Advent of Code puzzle \
description.

Your task:
1. Find ALL example inputs in the puzzle description
2. Find the expected answers for each example (for both Part 1 and Part 2 if \
available)
3. Preserve exact formatting of inputs (including newlines, spaces, etc.)
4. If Part 2 is not yet revealed or not mentioned, return empty string for part2
5. Return ALL examples found in the puzzle

The puzzle description is provided below in HTML format. Extract the examples and \
their expected outputs.

{puzzle_html}

Extract examples in the specified JSON format. Return an array of objects, each \
with "example", "part1", and "part2" fields."""


def extract_examples(year: int, day: int) -> list[dict[str, str]] | None:  # noqa: PLR0911
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable is not set", file=sys.stderr)
        return None

    model = os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL)

    try:
        puzzle_html = get_puzzle_html(year, day)
    except Exception as e:
        print(f"Error fetching puzzle: {e}", file=sys.stderr)
        return None

    prompt = create_extraction_prompt(puzzle_html)

    json_schema = {
        "type": "object",
        "properties": {
            "examples": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "example": {"type": "string"},
                        "part1": {"type": "string"},
                        "part2": {"type": "string"},
                    },
                    "required": ["example", "part1", "part2"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["examples"],
        "additionalProperties": False,
    }

    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(
                OPENROUTER_API_URL,
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "response_format": {
                        "type": "json_schema",
                        "json_schema": {"name": "aoc_examples", "strict": True, "schema": json_schema},
                    },
                },
            )
            response.raise_for_status()
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            result = json.loads(content)
            return result.get("examples", [])
    except httpx.HTTPStatusError as e:
        status_code = e.response.status_code
        response_text = e.response.text
        print(f"HTTP error from OpenRouter API: {status_code} - {response_text}", file=sys.stderr)
        return None
    except httpx.RequestError as e:
        print(f"Network error: {e}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}", file=sys.stderr)
        return None
    except KeyError as e:
        print(f"Unexpected response format: missing key {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


def parse_args() -> Namespace:
    year, day = get_current_date_est()

    parser = ArgumentParser(description="Extract examples from AOC puzzles using LLM")
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
    parser.add_argument("-o", "--output", type=str, help="Output file path (default: tests/YYYY/dDD.json)")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    year, day = args.year, args.day

    examples = extract_examples(year, day)
    if examples is None:
        sys.exit(1)

    if not examples:
        print("No examples extracted", file=sys.stderr)
        sys.exit(1)

    output_path = args.output or f"tests/{year}/d{day:02}.json"
    with Path(output_path).open("w") as output_file:
        json.dump(examples, output_file, indent=2)
        output_file.write("\n")

    print(f"Extracted {len(examples)} example(s) to {output_path}")


if __name__ == "__main__":
    main()
