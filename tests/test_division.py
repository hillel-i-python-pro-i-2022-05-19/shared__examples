import pytest

from app import division


@pytest.mark.parametrize(
    "a,b,result",
    [
        (6, 2, 3),
        (8, 4, 2),
        (5, 2, 2.5),
    ],
)
def test_division_good(a: int, b: int, result: int):
    assert division(a=a, b=b) == result


@pytest.mark.parametrize(
    "a,b",
    [
        (10, 0),
    ],
)
def test_division_bad(
    a: int,
    b: int,
):
    with pytest.raises(ZeroDivisionError):
        division(a=a, b=b)
