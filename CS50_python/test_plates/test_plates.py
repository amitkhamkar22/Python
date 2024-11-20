'''
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your
code per the below, wherein is_valid still expects a str as input and returns True
if that str meets all requirements and False if it does not, but main is only called
if the value of __name__ is "__main__":
def main():

def is_valid(s):

if __name__ == "__main__":
    main()
Then, in a file called test_plates.py, implement four or more functions that collectively test
your implementation of is_valid thoroughly, each of whose names should begin with test_
so that you can execute your tests with: pytest test_plates.py
'''

from plates import is_valid

# check min 2 and max 6 characters
def test_plateLength():
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("MH12345") == False
    assert is_valid("OUTATIME") == False
    assert is_valid('AB') == True

# check whether plates start with at least two letters
def test_twoLetters():
    assert is_valid("AB12") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A012") == False

#Numbers cannot be used in the middle of a plate; they must come at the end
def test_noMiddleNumbers():
    assert is_valid("CSS50") == True
    assert is_valid("CS50P") == False

#The first number used cannot be a ‘0’
def test_noFirstDigitZero():
    assert is_valid("CS05") == False

#No periods, spaces, or punctuation marks are allowed
def test_noPunctuation():
    assert is_valid("A.CD01") == False
    assert is_valid("A CD01") == False
    assert is_valid("ACD01!") == False
    assert is_valid("PI3.14") == False

#No biginning with non-alphabet charactor
def test_noAlphabeticalBeginning():
    assert is_valid("05CS") == False
    assert is_valid("") == False
    assert is_valid("_ABCD") == False
    assert is_valid("-ABCD") == False
    assert is_valid("1ABCDE") == False
    assert is_valid("22") == False
    assert is_valid("22A") == False

#No non-alphanumeric charactor in the string
def test_noAlphanumericChar():
    assert is_valid("~CD012") == False
    assert is_valid("!CD01*") == False