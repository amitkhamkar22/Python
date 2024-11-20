
#import numb3rs
from numb3rs import validate
#import re
import pytest


def main():
    #tests
    test_grater_than_255()
    test_more_than_3_digits()
    test_missing_digits()
    test_corner_cases()


def test_grater_than_255():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"256.255.255.255") == False
    assert validate(r"255.256.255.255") == False
    assert validate(r"255.255.256.255") == False
    assert validate(r"255.255.255.256") == False
    assert validate(r"512.521.521.521") == False


def test_more_than_3_digits():
    assert validate(r"1111.1.1.1") == False
    assert validate(r"1.1111.1.1") == False
    assert validate(r"1.1.1111.1") == False
    assert validate(r"1.1.1.1111") == False


def test_missing_digits():
    assert validate(r"1.1.1.1") == True
    assert validate(r"1.1.1.") == False
    assert validate(r"1.1.") == False
    assert validate(r"1.") == False
    assert validate(r"") == False

def test_corner_cases():
    assert validate(r"249.1.1.1") == True
    assert validate(r"291.1.1.1") == False
    assert validate(r"900.1.1.1") == False
    assert validate(r"1.900.1.1") == False
    assert validate(r"1.1.900.1") == False
    assert validate(r"1.1.1.900") == False
    assert validate(r"911.1.1.1") == False
    assert validate(r"191.1.1.1") == True
    assert validate(r"119.1.1.1") == True
    assert validate(r"1.911.1.1") == False
    assert validate(r"1.191.1.1") == True
    assert validate(r"1.119.1.1") == True
    assert validate(r"1.1.911.1") == False
    assert validate(r"1.1.191.1") == True
    assert validate(r"1.1.119.1") == True
    assert validate(r"1.1.1.911") == False
    assert validate(r"1.1.1.191") == True
    assert validate(r"1.1.1.119") == True
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False
    assert validate(r"1.1.1.1.1") == False


if __name__ == "__main__":
    main()