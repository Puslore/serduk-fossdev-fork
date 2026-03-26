import pytest
from src.calc import add

def test_add_basics():
    a, b = 10, 5
    result = add(a, b)
    assert result == 15

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (-1, 1, 0),
    (-5, -5, -10),
    (100, 200, 300),
    (1.5, 2.5, 4)
])
def test_add_various(a, b, expected):
    assert add(a, b) == expected