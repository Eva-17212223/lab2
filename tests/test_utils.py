import pytest
from src.utils import add, subtract, multiply, divide


# ---------- ADD ----------
def test_add_normal_cases():
    assert add(1, 2, 3, 4) == 10
    assert add(-1, 2, -3, 4) == 2
    assert add(0, 0, 0) == 0


def test_add_edge_cases():
    assert add() == 0
    # with one arg
    assert add(5) == 5


# ---------- SUBTRACT ----------
def test_subtract_normal_cases():
    assert subtract(10, 2, 3) == 5
    assert subtract(5, 5) == 0


def test_subtract_edge_cases():
    # with one argument
    assert subtract(7) == 7
    # without any argument
    assert subtract() == 0
    # negative numbers as arg
    assert subtract(-10, -5) == -5


# ---------- MULTIPLY ----------
def test_multiply_normal_cases():
    assert multiply(2, 3, 4) == 24
    assert multiply(5, 0) == 0
    assert multiply(-2, 3) == -6


def test_multiply_edge_cases():
    # without any argument
    assert multiply() == 0
    # with one argument
    assert multiply(9) == 9


# ---------- DIVIDE ----------
def test_divide_normal_cases():
    assert divide(20, 5) == 4
    assert divide(100, 2, 5) == 10
    assert pytest.approx(divide(7.5, 2.5)) == 3


def test_divide_edge_cases():
    # division by zero
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # with one argument
    assert divide(8) == 8

    # without any  argument
    assert divide() == 0

    # with negative numbers
    assert divide(-10, 2) == -5
