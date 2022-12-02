"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730570002"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """An empty Linked List should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_value_at_non_empty() -> None:
    """When given a non-empty list the value at the index should be returned."""
    linked_list = value_at(Node(10, Node(20, Node(30, None))), 1)
    assert linked_list == 20


def test_value_at_index_too_large() -> None:
    """When given an index too large returns an IndexError."""
    with pytest.raises(IndexError):
        value_at(Node(10, Node(20, Node(30, None))), 4)


def test_max_empty() -> None:
    """An empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """When given a non-empty list the largest value should be returned."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30


# def test_linkify_empty() -> None:
#     """An empty Linked List should raise a ValueError."""
    

# def test_linkify_non_empty() -> None:
#     """When given a non-empty list a Linked List of Nodes with the same values, in the same order, as the input list should be returned."""
#     items = [10, 20, 30, 40]
#     assert linkify(items[1]) == 20


# def test_scale_empty() -> None:
#     """An empty Linked List should raise a ValueError."""
    


# def test_scale_non_empty() -> None:
#     """When given a non-empty list the linked list is multiplied by a factor."""
#     assert scale(linkify([1, 2, 3]), 2) == [2, 4, 6]