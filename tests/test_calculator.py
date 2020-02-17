import pytest

from calculator.calc import Calculator

def test_add():
    c = Calculator()
    assert c.add(3, 4) == 7

def test_multiply():
    c = Calculator()
    assert c.multiply(3, 4) == 12

def test_substract():
    c = Calculator()
    assert c.substract(8,5) == 3

def test_divide():
    c = Calculator()
    assert c.divide(8,4) == 2
