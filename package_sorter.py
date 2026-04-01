from config import BULKY_VOLUME_THRESHOLD, BULKY_DIMENSION_THRESHOLD, HEAVY_MASS_THRESHOLD
import numbers

VALIDATE_ERROR = "Package dimensions and mass must be positive number"

def _is_number(value) -> None:
    if not isinstance(value, numbers.Number):
        raise ValueError(VALIDATE_ERROR)

def _is_positive(value) -> None:
    if value <= 0:
        raise ValueError(VALIDATE_ERROR)

def _is_bulky(width, height, length) -> bool:
    volume = width * height * length
    return (
        volume >= BULKY_VOLUME_THRESHOLD
        or width >= BULKY_DIMENSION_THRESHOLD
        or height >= BULKY_DIMENSION_THRESHOLD
        or length >= BULKY_DIMENSION_THRESHOLD
    )

def _is_heavy(mass) -> bool:
    return mass >= HEAVY_MASS_THRESHOLD

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
