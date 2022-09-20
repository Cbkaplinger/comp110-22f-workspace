"""Functions with lists."""

__author__ = "730570002"


def all(list: list[int], num: int) -> bool:
    """Checks if all the numbers in the list are equal to the num."""
    index: int = 0
    in_index: bool = False

    if len(list) == 0:
        return False
    else:
        while index < len(list):
            if num == list[index]:
                in_index = True
            else:
                in_index = False
                return False
            index += 1

        if in_index is True:
            return True
        else:
            return False


def max(max_list: list[int]) -> int:
    """In a list of integers it outputs the max of the list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index: int = 0
        maximum: int = max_list[0]
        while index < len(max_list):
            if maximum < max_list[index]:
                maximum = max_list[index]
            index += 1
        return maximum


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks if two lists are equivalent to each other."""
    index: int = 0
    equivalent: bool = False

    if len(first_list) + len(second_list) == 0:
        return True
    else:
        if len(first_list) == 0 or len(second_list) == 0:
            return False
        if len(first_list) == len(second_list):
            while index < len(first_list):
                if first_list[index] == second_list[index]:
                    equivalent = True
                else:
                    equivalent = False
                index += 1
            if equivalent is True:      
                return True
            else:
                return False
        else:
            return False