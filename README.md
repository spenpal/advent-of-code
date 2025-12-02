# Advent of Code

I started doing Advent of Code hoping to become a better Python programmer than the year before. Feel free to check my progress and how my code has evolved! I am constantly learning new ways to program in Python, and using efficient and interesting tricks to make my code more readable, writeable, and exploit a faster runtime. You might find a thing or two that you have never seen used practically in Python before 👀...

I don't use comments for the majority of my code, as the code should be well written enough that it explains itself (_at least in the context of knowing the puzzle_).

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
  - [Running Solutions](#running-solutions)
  - [Testing](#testing)
  - [Submitting Solutions](#submitting-solutions)
  - [Generating Templates](#generating-templates)
  - [LLM-Based Example Extraction](#llm-based-example-extraction)
  - [Linting & Formatting](#linting-formatting)
  - [Quick Reference](#quick-reference)
- [Example Workflow](#example-workflow)
- [Project Structure](#project-structure)
- [Solution File Format](#solution-file-format)
- [Test File Format](#test-file-format)

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management. To get started:

1. Install dependencies and setup pre-commit hooks:

   ```bash
   make setup
   ```

   This will:

   - Install all project dependencies (including dev dependencies)
   - Set up pre-commit hooks for code quality checks

2. Configure your Advent of Code session token:

   - Get your session token from your browser's cookies (visit adventofcode.com and check cookies for `session`)
   - For step-by-step instructions, see [this guide](https://github.com/wimglenn/advent-of-code-wim/issues/1)
   - You can set it in one of three ways:
     1. **In `.env` file (recommended)**: Copy `.env.example` to `.env` and set `AOC_SESSION=your_token_here`
     2. **As environment variable**: `export AOC_SESSION="your_token_here"`
     3. **In config file**: `echo "your_token_here" > ~/.config/aocd/token`

3. (Optional) Configure OpenRouter API key for LLM example extraction:
   - Get your API key from [OpenRouter](https://openrouter.ai/keys)
   - Copy `.env.example` to `.env` and set your `OPENROUTER_API_KEY`:
     ```bash
     cp .env.example .env
     # Edit .env and set your OPENROUTER_API_KEY and AOC_SESSION
     ```

## Usage

All commands use Makefile aliases that automatically run in the project's virtual environment via `uv run`.

**Important:** All commands use **EST (Eastern Standard Time)** to determine the "current day". Puzzles release at 12:00 AM EST each day. If you're in a different timezone or want to generate templates ahead of time, you must explicitly specify the day using `DAY=N`.

### Running Solutions

Run a solution for the current day:

```bash
make run
```

Run a solution for a specific year and day:

```bash
make run YEAR=2024 DAY=5
```

### Testing

Test your solution against example inputs:

```bash
make test              # Test both parts
make test1             # Test part 1 only
make test2             # Test part 2 only
```

With specific year/day:

```bash
make test YEAR=2024 DAY=5
make test1 YEAR=2024 DAY=5
make test2 YEAR=2024 DAY=5
```

### Submitting Solutions

Submit your solution to Advent of Code:

```bash
make submit1           # Submit part 1 (current day)
make submit2           # Submit part 2 (current day)
```

With specific year/day:

```bash
make submit1 YEAR=2024 DAY=5
make submit2 YEAR=2024 DAY=5
```

### Generating Templates

Generate solution and test templates. During the AOC active period (Dec 1-25), `make gen` defaults to the current day **in EST timezone**.

**Timezone Note:** If you're generating templates before midnight EST (e.g., 11:00 PM EST for a puzzle that releases at 12:00 AM EST), the script will see it as the previous day. You must explicitly specify the day you want to generate:

```bash
make gen               # Generate current day (in EST)
make gen DAY=5         # Generate specific day (use this if generating ahead of time)
make gen DAY="1 5"     # Generate range of days (1 through 5)
make gen YEAR=2024 DAY=5  # Generate specific year/day
make gen YEAR=2024 DAY="1 5"  # Generate range for specific year
```

**Example:** If it's 11:00 PM EST on Dec 1st and you want to generate templates for Day 2 (which releases at 12:00 AM EST), run:

```bash
make gen DAY=2
```

### LLM-Based Example Extraction

`make gen` automatically attempts to extract examples using AI via OpenRouter. If extraction fails (e.g., API key not set, network error, or puzzle not unlocked), it falls back to creating an empty template.

```bash
# Generate templates (automatically attempts LLM extraction)
make gen DAY=5

# Or extract examples for existing puzzle files
make extract DAY=5
```

**Note:** If extraction fails, an empty template will be created (you can fill it manually). The LLM extraction uses structured outputs to ensure the examples match the required JSON format.

**Configuration:**

- Copy `.env.example` to `.env` and set your `OPENROUTER_API_KEY`
- Optionally set `OPENROUTER_MODEL` to use a different model

### Linting & Formatting

Check code quality and format code:

```bash
make lint              # Check code with ruff
make lint-fix          # Check and auto-fix code with ruff
make format            # Format code with ruff
make format-check      # Check formatting without making changes
```

### Quick Reference

```bash
make help              # Show all available commands
make run               # Run current day
make test              # Test current day (both parts)
make test1             # Test current day (part 1)
make test2             # Test current day (part 2)
make submit1           # Submit part 1 (current day)
make submit2           # Submit part 2 (current day)
make gen               # Generate templates for current day (with LLM extraction)
make extract           # Extract examples for existing puzzles
make lint              # Check code with ruff
make lint-fix          # Check and auto-fix code with ruff
make format            # Format code with ruff
make format-check      # Check formatting without making changes
```

All commands support `YEAR=YYYY` and `DAY=N` (or `DAY="N M"` for ranges) to specify a different year/day.

## Example Workflow

Here's a typical workflow when starting a new Advent of Code day:

### 1. Generate Templates

Generate the solution and test templates for the day you want to work on:

```bash
# If it's after midnight EST (puzzle is already released)
make gen

# If generating ahead of time (before midnight EST), specify the day
make gen DAY=5
```

This creates:

- `src/YYYY/dDD.py` - Solution template
- `tests/YYYY/dDD.json` - Test template

### 2. Read the Puzzle

Visit [adventofcode.com](https://adventofcode.com) and read the puzzle description. Copy the example input into `tests/YYYY/dDD.json`.

### 3. Implement Your Solution

Edit `src/YYYY/dDD.py`:

- Implement `parse()` to parse the input data
- Implement `part1()` to solve part 1
- Implement `part2()` to solve part 2

### 4. Test Your Solution

Test against the example inputs:

```bash
make test              # Test both parts
make test1             # Test only part 1
make test2             # Test only part 2
```

### 5. Run on Real Input

Once tests pass, run on the actual puzzle input:

```bash
make run                  # Run current day
make run YEAR=2024 DAY=5  # Run specific day
```

### 6. Submit Your Answer

After verifying the output looks correct, submit:

```bash
make submit1           # Submit part 1
make submit2           # Submit part 2
```

### 7. Format & Lint (Optional)

Before committing, format and lint your code:

```bash
make format            # Format code
make lint-fix          # Check and auto-fix linting issues
```

## Project Structure

```
advent-of-code/
├── src/                # Solution files
│   ├── 2021/
│   │   ├── d01.py      # Day 1 solution
│   │   └── ...
│   ├── 2022/
│   └── ...
├── tests/              # Test cases (example inputs/answers)
│   ├── 2021/
│   │   ├── d01.json
│   │   └── ...
│   └── ...
├── templates/          # Template files
│   ├── day.py         # Solution template
│   └── examples.json  # Test template
├── scripts/
│   └── generate.py    # Template generator
└── main.py            # Main runner script
```

## Solution File Format

Each solution file (`src/YYYY/dDD.py`) must implement three functions:

1. **`parse(data: str) -> dict[int, tuple]`**: Parses the input data and returns a dictionary mapping part numbers (1, 2) to tuples of parsed data for each part.

2. **`part1(...)`**: Solves part 1 of the puzzle. Receives unpacked arguments from `parse()[1]`.

3. **`part2(...)`**: Solves part 2 of the puzzle. Receives unpacked arguments from `parse()[2]`.

### Parameter Naming

**Important:** The template uses generic parameter names (`data`), but you should **rename them to be descriptive** based on what your `parse()` function returns. The tuple returned by `parse()` gets unpacked when calling `part1()` and `part2()`, so use meaningful names that reflect the actual data structure.

**Example with multiple parameters:**

```python
def parse(data: str) -> dict[int, tuple]:
    numbers = [int(x) for x in data.split()]
    names = data.strip().splitlines()
    return {1: (numbers, names), 2: (numbers, names)}

def part1(numbers: list[int], names: list[str]) -> int:
    # Use numbers and names here
    return result

def part2(numbers: list[int], names: list[str]) -> int:
    # Use numbers and names here
    return result
```

**Example with single parameter:**

```python
def parse(data: str) -> dict[int, tuple]:
    lines = data.strip().splitlines()
    return {1: (lines,), 2: (lines,)}

def part1(lines: list[str]) -> int:
    # Use lines here
    return result

def part2(lines: list[str]) -> int:
    # Use lines here
    return result
```

**Best practices:**

- Use descriptive names that indicate what the data represents (e.g., `ids`, `grid`, `instructions`, `pairs`)
- Match the number of parameters to the tuple size returned by `parse()`
- Add type hints to make the code more readable and catch errors early

## Test File Format

Test files (`tests/YYYY/dDD.json`) contain example inputs and expected outputs:

```json
[
  {
    "example": "input data here",
    "part1": "expected output for part 1",
    "part2": "expected output for part 2"
  }
]
```

You can add multiple test cases by adding more objects to the array.
