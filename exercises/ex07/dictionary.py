"""Dictionary Utilities."""

__author__ = "730570002"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Switches the values and keys when given a dictionary."""
    new_dictionary = {value: key for key, value in dictionary.items()}
    return new_dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """When given a dictionary returns a string with the most common color."""
    new_dictionary: dict[str, str] = {}
    i: int = 0
    common_color: str = ""
    for key in dictionary:
        if dictionary[key] in new_dictionary:
            new_dictionary[dictionary[key]] += 1
        else:
            new_dictionary[dictionary[key]] = 1

    for key in new_dictionary:
        if i < new_dictionary[key]:
            i = new_dictionary[key]
            common_color = key
    return common_color


def count(list: list[str]) -> dict[str, int]:
    """When given a list returns a dictionary of an item and how many times the item appears."""
    new_dictionary: dict[str, int] = {}
    i: int = 0
    variable: int = 0
    counter: int = 0
    values: str = ""

    while variable < len(list):
        values = list[variable]
        while i < len(list):
            if list[i] == values:
                counter += 1
            i += 1
        new_dictionary[list[variable]] = counter
        counter = 0
        i = 0
        variable += 1
    return new_dictionary