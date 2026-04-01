from config import BULKY_VOLUME_THRESHOLD, BULKY_DIMENSION_THRESHOLD, HEAVY_MASS_THRESHOLD

VALIDATE_ERROR = "Package dimensions and mass must be positive number"


def _validate(width: int, height: int, length: int, mass: int) -> None:
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError(VALIDATE_ERROR)


def _is_bulky(width: int, height: int, length: int) -> bool:
    volume = width * height * length
    return (
        volume >= BULKY_VOLUME_THRESHOLD
        or width >= BULKY_DIMENSION_THRESHOLD
        or height >= BULKY_DIMENSION_THRESHOLD
        or length >= BULKY_DIMENSION_THRESHOLD
    )


def _is_heavy(mass: int) -> bool:
    return mass >= HEAVY_MASS_THRESHOLD


def sort(width: int, height: int, length: int, mass: int) -> str:
    _validate(width, height, length, mass)

    bulky = _is_bulky(width, height, length)
    heavy = _is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
