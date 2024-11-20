from jar import Jar
import pytest


def test_init():
    jar = Jar(capacity = 12)
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(capacity = 12)
    with pytest.raises(ValueError):
        assert jar.deposit(13)

def test_withdraw():
    jar = Jar(capacity = 12)
    with pytest.raises(ValueError):
        assert jar.withdraw(13)
