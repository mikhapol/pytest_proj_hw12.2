import pytest

from utils.arrs import get


@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, "test", 3),
    ([], 0, "test", "test"),
])
def test_get_parametrize(array, index, default, expected):
    assert get(array, index, default) == expected

