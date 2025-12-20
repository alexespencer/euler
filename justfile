# justfile for euler - linting stage using ruff

# Default target
default: lint-stage

format:
	@echo "Formatting Python files with ruff..."
	@uv run ruff check --fix .
	@uv run ruff format .

check:
	@echo "Running ruff checks..."
	@uv run ruff check .

lint-stage:
	@echo "Running lint stage: format then check"
	@just format
	@just check
