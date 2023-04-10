import pytest

from utils.arrs import get


@pytest.fixture('array, index, default, expected', [
    ([1, 2, 3], 1, "test", 3),
    ([], 0, "test", "test"),
])
def test_types_count(array, index, default, expected):
    assert get(array, index, default) == expected


