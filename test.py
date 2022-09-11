import pytest
from data.testdata import *


#INT
@pytest.mark.parametrize("nul, points", [(0, points1),
                                         (0, points2),
                                         (0, points3),
                                         (0, points4)])
def test_int1(nul, points):
    try:
        assert nul < points
        print(f'Число "{points}" - положительное')
    except AssertionError:
        print(f'Число "{points}" - отрицательное')


# LIST
def list_reverse(l):
    return l.reverse()


def list_sort(l):
    return l.sort()


@pytest.mark.parametrize("l, expected", [([3, 4, 5, 3, 9], [9, 3, 5, 4, 3]), ([3, 4, 5, 3, 9], [9, 3, 5, 4, 3])])
def test_list_reverse(l, expected):
    list_reverse(l)
    assert len(l) == len(expected)
    for i in range(len(l)):
        assert l[i] == expected[i]


def test_list_sort():
    list_sort(l)
    for i in range(1, len(l)):
        assert l[i] >= l[i-1]


# SET
def test_set1():
    assert x.union(y) == (x | y)


def test_set2():
    assert x.intersection(y) == {3}
