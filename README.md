# Package Sorter

This project classifies packages into one of three stacks:

- `STANDARD`
- `SPECIAL`
- `REJECTED`

The classification is based on package dimensions and mass.

## Rules

A package is considered **bulky** if:

- its volume (`width × height × length`) is greater than or equal to `BULKY_VOLUME_THRESHOLD`, or
- any one of its dimensions is greater than or equal to `BULKY_DIMENSION_THRESHOLD`

A package is considered **heavy** if:

- its mass is greater than or equal to `HEAVY_MASS_THRESHOLD`

## Dispatching Logic

- `STANDARD` — package is neither bulky nor heavy
- `SPECIAL` — package is either bulky or heavy
- `REJECTED` — package is both bulky and heavy

## Validation

All input values must be:

- numeric
- greater than zero

If any value is invalid, the function raises:

```python
ValueError("Package dimensions and mass must be positive number")
```

## Project Structure

```text
.
├── config.py
├── main.py
├── package_sorter.py
├── README.md
└── tests
    └── test_package_sorter.py
```

### Files Description

- `package_sorter.py` — contains the main sorting logic and helper validation/check functions
- `config.py` — stores threshold constants used by the sorter
- `main.py` — optional entry point for running the program manually
- `tests/test_package_sorter.py` — unit tests for package classification and validation
- `README.md` — project documentation

## Configuration

Threshold values are imported from `config.py`:

```python
from config import BULKY_VOLUME_THRESHOLD, BULKY_DIMENSION_THRESHOLD, HEAVY_MASS_THRESHOLD
```

Example constants may look like:

```python
BULKY_VOLUME_THRESHOLD = 1_000_000
BULKY_DIMENSION_THRESHOLD = 150
HEAVY_MASS_THRESHOLD = 20
```

## Main Function

```python
sort(width, height, length, mass) -> str
```

### Parameters

- `width` — package width
- `height` — package height
- `length` — package length
- `mass` — package mass

### Returns

A string representing the package stack:

- `"STANDARD"`
- `"SPECIAL"`
- `"REJECTED"`

## Example Usage

```python
from package_sorter import sort

result = sort(100, 100, 100, 10)
print(result)
```

## Implementation Details

The implementation is split into small helper functions so that validation and business rules stay simple and easy to test.

### 1. Number Validation

```python
def _is_number(value) -> None:
    if not isinstance(value, numbers.Number):
        raise ValueError(VALIDATE_ERROR)
```

This function checks that each input is a numeric value.

### 2. Positive Value Validation

```python
def _is_positive(value) -> None:
    if value <= 0:
        raise ValueError(VALIDATE_ERROR)
```

This function ensures that all dimensions and mass are greater than zero.

### 3. Bulky Package Check

```python
def _is_bulky(width, height, length) -> bool:
    volume = width * height * length
    return (
        volume >= BULKY_VOLUME_THRESHOLD
        or width >= BULKY_DIMENSION_THRESHOLD
        or height >= BULKY_DIMENSION_THRESHOLD
        or length >= BULKY_DIMENSION_THRESHOLD
    )
```

A package is bulky if:

- the total volume reaches the configured bulky volume threshold, or
- at least one dimension reaches the configured bulky dimension threshold

### 4. Heavy Package Check

```python
def _is_heavy(mass) -> bool:
    return mass >= HEAVY_MASS_THRESHOLD
```

A package is heavy if its mass reaches the configured heavy mass threshold.

### 5. Sorting Logic

```python
def sort(width, height, length, mass) -> str:
    for x in (width, height, length, mass):
        _is_number(x)
        _is_positive(x)

    bulky = _is_bulky(width, height, length)
    heavy = _is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
```

The function works in four steps:

1. validates all input values
2. determines whether the package is bulky
3. determines whether the package is heavy
4. returns the correct stack based on the rules

## Example Cases

### Standard package

```python
sort(10, 20, 30, 5)
# STANDARD
```

### Bulky only

```python
sort(200, 20, 30, 5)
# SPECIAL
```

### Heavy only

```python
sort(10, 20, 30, 25)
# SPECIAL
```

### Bulky and heavy

```python
sort(200, 200, 200, 25)
# REJECTED
```

### Invalid input

```python
sort(-1, 20, 30, 5)
# raises ValueError
```

## Running Tests

If you use `pytest`, run:

```bash
pytest
```

Or run a specific test file:

```bash
pytest tests/test_package_sorter.py
```

## Notes

- the code uses helper func