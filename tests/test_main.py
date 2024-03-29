"""Tests for main module."""

from fabric_calc.fabric_calc import (
    bin_packing_calculator,
    calc_material_dimensions,
    check_answer,
    combine_rectangles,
    calculate,
    get_median,
    inches_to_yards,
    max_size,
    yard_to_inches,
)


def test_max_size():
    """Test max size function."""
    assert max_size([(10, 1), (2, 100)]) == 110


def test_yard_to_inches():
    """Test yards to inches function."""
    assert yard_to_inches(1) == 36
    assert yard_to_inches(2) == 72


def test_inches_to_yards():
    """Test inches to yards function."""
    assert inches_to_yards(0) == 0
    assert inches_to_yards(1) == 1
    assert inches_to_yards(36) == 1
    assert inches_to_yards(37) == 2
    assert inches_to_yards(28800) == 800
    assert inches_to_yards(28801) == 801


def test_get_median():
    """Test Get median function."""
    assert get_median((1, 5)) == 3
    assert get_median((1, 6)) == 3
    assert get_median((1, 1)) == 1


def test_check_answer():
    """Test Check Answer function."""
    rectangles = [
        (66, 36),
        (66, 36),
        (66, 36),
    ]

    assert check_answer(rectangles, 3) == (True, 1)
    assert check_answer(rectangles, 1) == (False, 3)

    rectangles = [
        (66, 36),
    ]
    assert check_answer(rectangles, 1) == (True, 1)

    rectangles = [
        (33, 36),
        (33, 36),
        (33, 36),
        (33, 36),
    ]

    assert check_answer(rectangles, 3) == (True, 1)


def test_calc_material_dimensions():
    """Test materials dimension calc."""
    assert calc_material_dimensions(1) == (66, 36)
    assert calc_material_dimensions(2) == (66, 72)
    assert calc_material_dimensions(100) == (66, 3600)


def test_bin_packing_calculator():
    """Test Bin Packing Calculator."""
    rectangles = [
        (32, 32),
        (32, 32),
        (32, 32),
        (32, 32),
    ]

    material = calc_material_dimensions(2)
    assert bin_packing_calculator(rectangles, material) == 1

    rectangles = [
        (33, 36),
        (33, 36),
        (33, 36),
        (33, 36),
    ]

    material = calc_material_dimensions(3)
    assert bin_packing_calculator(rectangles, material) == 1


def test_calculate():
    """Test Fabric Calc."""
    rectangles = [
        (32, 65, 1),
    ]
    print(check_answer(rectangles, 1))
    print(calc_material_dimensions(1))
    print(bin_packing_calculator(rectangles, calc_material_dimensions(1)))
    assert calculate(rectangles) == 1


def test_combine_rectangles():
    assert combine_rectangles([(32, 65, 1)]) == [(32, 65)]
    assert combine_rectangles([(32, 65, 3)]) == [(32, 65), (32, 65), (32, 65)]
    assert combine_rectangles([(32, 65, 3), (32, 65, 2)]) == [
        (32, 65),
        (32, 65),
        (32, 65),
        (32, 65),
        (32, 65),
    ]
    assert combine_rectangles([(32, 65, 3), (31, 65, 2)]) == [
        (32, 65),
        (32, 65),
        (32, 65),
        (31, 65),
        (31, 65),
    ]
