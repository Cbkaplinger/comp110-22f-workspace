"""Tests the functions from ex05."""

__author__ = "730570002"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_both() -> None:
    """Evens and odds."""
    list: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(list) == [2, 4, 6, 8, 10]


def test_only_evens_empty() -> None:
    """Empty list."""
    list: list[int] = []
    assert only_evens(list) == []


def test_only_evens_odds() -> None:
    """Odds only."""
    list: list[int] = [3, 5, 7, 9]
    assert only_evens(list) == []


def test_concat_two_lists() -> None:
    """Two full lists with integers."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_empty_list() -> None:
    """One empty list and one full list."""
    list1: list[int] = []
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [4, 5, 6]


def test_concat_two_empty_lists() -> None:
    """Two empty lists."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_sub_empty_list_same_start_and_end() -> None:
    """Blank list with the same start and end."""
    list: list[int] = []
    start: int = 1
    end: int = 1
    assert sub(list, start, end) == []


def test_sub_full_list_same_start_and_end() -> None:
    """Full list with the same start and end."""
    list: list[int] = [1, 2, 3]
    start: int = 1
    end: int = 1
    assert sub(list, start, end) == []


def test_sub_empty_list_different_start_and_end() -> None:
    """Empty list with the different start and end."""
    list: list[int] = []
    start: int = 0
    end: int = 4
    assert sub(list, start, end) == []


def test_sub_full_list_negative_start() -> None:
    """Full list with a negative start."""
    list: list[int] = [1, 2, 3]
    start: int = -1
    end: int = 3
    assert sub(list, start, end) == [1, 2, 3]


def test_sub_full_list_end_longer_than_list() -> None:
    """Full list with an end longer than the list."""
    list: list[int] = [1, 2, 3]
    start: int = 1
    end: int = 6
    assert sub(list, start, end) == [2, 3]


def test_sub_regular() -> None:
    """Normal everything."""
    list: list[int] = [1, 2, 3]
    start: int = 1
    end: int = 3
    assert sub(list, start, end) == [2, 3]