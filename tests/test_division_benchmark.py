import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from app import division


@pytest.mark.parametrize(
    "a,b,result",
    [
        (6, 2, 3),
        (8, 4, 2),
        (5, 2, 2.5),
    ],
)
def test_division_good(a: int, b: int, result: int, benchmark: BenchmarkFixture):
    result_ = benchmark(
        division,
        a,
        b,
    )
    assert result_ == result
