from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -1, 3) == []     # проверка 40-43
    assert arrs.my_slice([], 1, 3) == []                # проверка 33
    assert arrs.my_slice([1], -5, 1) == [1]             # проверка 41
