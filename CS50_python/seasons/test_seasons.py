import pytest
from seasons import time_in_minutes

def main():
    test_correct_date()
    test_date_incorrect()
    test_date_format_incorrect()

#verify that correct dates provide desired output
def test_correct_date():

    assert time_in_minutes("2022-08-23") == "Five hundred twenty-five thousand, six hundred minutes"

    assert time_in_minutes("2021-08-23") == "One million, fifty-one thousand, two hundred minutes"

#verify that leap year error and future birth date results in exiting with message
def test_date_incorrect():

    with pytest.raises(SystemExit):
        assert time_in_minutes("2019-02-29")

    with pytest.raises(SystemExit):
        assert time_in_minutes("2030-02-12")

#veirfy that dates in incorrect format result in exiting with message
def test_date_format_incorrect():
    
    with pytest.raises(SystemExit):
        assert time_in_minutes("200-02-12")

    with pytest.raises(SystemExit):
        assert time_in_minutes("2000-2-12")

    with pytest.raises(SystemExit):
        assert time_in_minutes("2000-02-112")

    with pytest.raises(SystemExit):
        assert time_in_minutes("2000 02-12")

    with pytest.raises(SystemExit):
        assert time_in_minutes("2000-02 12")

if __name__ == "__main__":
    main()