import pytest

import simplecalculator 

def test_add():

    result = simplecalculator.add(6, 9)
    assert result == 15



def test_subtract():
    
    result = simplecalculator.subtract(12, 6)
    assert result == 6


def test_multiply():

    result= simplecalculator.multiply(8, 7)
    assert result == 56


def test_divide():

    ans = simplecalculator.divide(16, 2)
    assert ans == 8