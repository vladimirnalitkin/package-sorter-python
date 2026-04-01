import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from package_sorter import sort


@pytest.mark.parametrize("width,height,length,mass,expected", [
    (1, 1, 1, 1, "STANDARD"),           # not bulky, not heavy
    (10, 20, 30, 5, "STANDARD"),         # not bulky, not heavy
    (10, 20, 30, 20, "SPECIAL"),         # not bulky, heavy
    (100, 100, 100, 10, "SPECIAL"),      # bulky (volume=1M exactly), not heavy
    (150, 10, 10, 10, "SPECIAL"),        # bulky (width>=150), not heavy
    (10, 150, 10, 10, "SPECIAL"),        # bulky (height>=150), not heavy
    (10, 10, 150, 10, "SPECIAL"),        # bulky (length>=150), not heavy
    (100, 100, 100, 20, "REJECTED"),     # bulky and heavy
    (10, 151, 10, 25, "REJECTED"),       # bulky (height) and heavy
    (50000, 50000, 50000, 1, "SPECIAL"), # bulky (volume + dims), not heavy
])
def test_sort_packages_correctly(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected


@pytest.mark.parametrize("width,height,length,mass,expected", [
    (100, 100, 100, 19, "SPECIAL"),  # bulky (volume=1M exactly), not heavy
    (10, 10, 10, 20, "SPECIAL"),     # not bulky, heavy (mass=20 exactly)
    (150, 1, 1, 19, "SPECIAL"),      # bulky (width=150 exactly), not heavy
    (100, 100, 100, 20, "REJECTED"), # bulky and heavy (both at threshold)
])
def test_threshold_values_are_inclusive(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected


@pytest.mark.parametrize("width", [0, -1, -10])
def test_raises_for_non_positive_width(width):
    with pytest.raises(ValueError):
        sort(width, 10, 10, 10)


@pytest.mark.parametrize("height", [0, -1, -10])
def test_raises_for_non_positive_height(height):
    with pytest.raises(ValueError):
        sort(10, height, 10, 10)


@pytest.mark.parametrize("length", [0, -1, -10])
def test_raises_for_non_positive_length(length):
    with pytest.raises(ValueError):
        sort(10, 10, length, 10)


@pytest.mark.parametrize("mass", [0, -1, -5])
def test_raises_for_non_positive_mass(mass):
    with pytest.raises(ValueError):
        sort(10, 10, 10, mass)
