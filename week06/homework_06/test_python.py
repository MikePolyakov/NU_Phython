"""
тесты для встроенных функций filter, map, sorted
"""
from math import pi, sqrt, pow, hypot


def test_filter():
    list_for_test = [-1, 0, 1]
    assert list(filter(None, list_for_test)) == [-1, 1]
    assert list(filter(lambda x: x > 0, list_for_test)) == [1]


def test_map():
    list_for_test = [-1, 0, 1]
    assert list(map(lambda x: x**2, list_for_test)) == [1, 0, 1]


def test_sorted():
    list_for_test = [1, 0, -1]
    assert list(sorted(list_for_test)) == [-1, 0, 1]


"""
тесты для функций из библиотеки math: pi, sqrt, pow, hypot
"""


def test_pi():
    assert round(pi, 2) == 3.14
    assert round(pi, 4) == 3.1416


def test_sqrt():
    list_for_test = [1, 4, 9]
    list_with_results = [1, 2, 3]
    for i in range(len(list_for_test)):
        assert sqrt(list_for_test[i]) == list_with_results[i]


def test_pow():
    list_for_test = [1, 2, 3]
    list_with_results = [1, 4, 9]
    for i in range(len(list_for_test)):
        assert pow(list_for_test[i], 2) == list_with_results[i]


def test_hypot():
    list_for_test = [[3, 4], [5, 12]]
    list_with_results = [5, 13]
    for i in range(len(list_for_test)):
        assert hypot(list_for_test[i][0], list_for_test[i][1]) == list_with_results[i]

