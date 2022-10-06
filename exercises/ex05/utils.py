"""More utility functions."""

__author__ = "730570002"


def only_evens(list: list[int]):
    """When given a list returns only even values."""
    new_list: list[int] = []
    index: int = 0

    while index < len(list):
        if list[index] % 2 == 0:
            new_list.append(list[index])
        index += 1
        
    return new_list


def concat(list1: list[int], list2: list[int]):
    """Combines two lists into one list."""
    index: int = 0
    new_list: list[int] = []

    while index < len(list1):
        new_list.append(list1[index])
        index += 1
    
    index = 0

    while index < len(list2):
        new_list.append(list2[index])
        index += 1

    return new_list


def sub(list: list[int], start: int, end: int):
    """Prints out all numbers in a list between a specified starting index and a specified ending index."""
    new_list: list[int] = []

    if len(list) == 0:
        return new_list
    else:
        if start < 0:
            start = 0
        if end > len(list):
            end = len(list)
        
        while start < end:
            new_list.append(list[start])
            start += 1
    
    return new_list