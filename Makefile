.PHONY: setup run test test1 test2 submit1 submit2 gen gen-llm extract lint lint-fix format format-check help

# Setup: Install dependencies and configure pre-commit hooks
setup:
	@echo "Installing dependencies..."
	@uv sync
	@echo "Setting up pre-commit hooks..."
	@uv run pre-commit install
	@echo "Setup complete!"

# Run solution (defaults to current day)
run:
	@uv run python main.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY))

# Test solutions
test:
	@uv run python main.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY)) -t

test1:
	@uv run python main.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY)) -t 1

test2:
	@uv run python main.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY)) -t 2

# Submit solutions
submit1:
	@uv run python main.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY)) -s 1

submit2:
	@uv run python main.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY)) -s 2

# Generate templates (defaults to current day during AOC active period)
gen:
	@uv run python scripts/generate.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY))

# Generate with LLM extraction
gen-llm:
	@uv run python scripts/generate.py --llm-extract $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY))

# Extract examples for existing puzzles
extract:
	@uv run python scripts/extract_examples.py $(if $(YEAR),-y $(YEAR)) $(if $(DAY),-d $(DAY))

# Linting
lint:
	@uv run ruff check .

lint-fix:
	@uv run ruff check --fix .

# Formatting
format:
	@uv run ruff format .

format-check:
	@uv run ruff format --check .

# Help
help:
	@echo "Advent of Code Makefile Commands:"
	@echo ""
	@echo "Setup (run once):"
	@echo "  make setup            - Install dependencies and setup pre-commit hooks"
	@echo ""
	@echo "Running Solutions:"
	@echo "  make run              - Run current day's solution"
	@echo "  make run YEAR=2024 DAY=5  - Run specific year/day"
	@echo ""
	@echo "Testing:"
	@echo "  make test             - Test current day (both parts)"
	@echo "  make test1            - Test current day (part 1)"
	@echo "  make test2            - Test current day (part 2)"
	@echo "  make test YEAR=2024 DAY=5  - Test specific year/day"
	@echo ""
	@echo "Submitting:"
	@echo "  make submit1          - Submit part 1 (current day)"
	@echo "  make submit2          - Submit part 2 (current day)"
	@echo "  make submit1 YEAR=2024 DAY=5  - Submit part 1 (specific year/day)"
	@echo ""
	@echo "Generating Templates:"
	@echo "  make gen              - Generate current day"
	@echo "  make gen DAY=5         - Generate specific day"
	@echo "  make gen DAY=\"1 5\"     - Generate range of days"
	@echo "  make gen YEAR=2024 DAY=5  - Generate specific year/day"
	@echo "  make gen-llm          - Generate with LLM example extraction"
	@echo "  make extract          - Extract examples for existing puzzles"
	@echo ""
	@echo "Linting & Formatting:"
	@echo "  make lint             - Check code with ruff"
	@echo "  make lint-fix         - Check and auto-fix code with ruff"
	@echo "  make format           - Format code with ruff"
	@echo "  make format-check     - Check formatting without making changes"
	@echo ""
	@echo "Note: YEAR and DAY default to current date in EST timezone"

