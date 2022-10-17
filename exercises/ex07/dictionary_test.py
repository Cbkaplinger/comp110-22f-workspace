"""Testing the dictionary utilities."""

__author__ = "730570002"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None:
    """When the dictionary is empty."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert() -> None:
    """When the dictionary is empty."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert_full() -> None:
    """When the dictionary has mulitple keys and values."""
    dictionary: dict[str, str] = {"a": "b", "e": "v"}
    assert invert(dictionary) == {"b": "a", "v": "e"}


def test_invert_KeyError() -> None:
    """Raises a key error when multiples values given are the same."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        assert invert(my_dictionary) == KeyError


def test_favorite_color_empty() -> None:
    """When the dictionary is empty."""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == {}


def test_favorite_color_same() -> None:
    """When the dictionary has all of the same colors."""
    dictionary: dict[str, str] = {'John': 'blue', 'Joseph': 'blue', 'Mary': 'blue'}
    assert favorite_color(dictionary) == {}


def test_favorite_color_tie() -> None:
    """When the dictionary has a tie."""
    dictionary: dict[str, str] = {'John': 'blue', 'Joseph': 'red'}
    assert favorite_color(dictionary) == {}


def test_count_empty() -> None:
    """When the list is empty."""
    list: list[str] = {}
    assert count(list) == {}


def test_count_small_list() -> None:
    """When a small list is given."""
    list: list[str] = {"a", "b", "c"}
    assert count(list) == {"a": 1, "b": 1, "c": 1}


def test_count_large_list() -> None:
    """When a large list is given."""
    list: list[str] = {"a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c"}
    assert count(list) == {"a": 4, "b": 4, "c": 4}