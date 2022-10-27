"""Dictionary related utility functions."""

__author__ = "730570002"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str: str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns a list of all the values in a column."""
    result: list[str] = []

    for row in table:
        result.append(row[column])

    return result


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table from row oriented to column oriented."""
    result: dict[str, list[str]] = {}
    row1: dict[str, str] = rows[0]

    for column in row1:
        result[column] = column_values(rows, column)
    
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns the amount of rows designated in the function."""
    if rows > len(table):
        return table

    result: dict[str, list[str]] = {}

    for key in table:
        row: list[str] = []
        i: int = 0

        while i < rows:
            row.append(table[key][i])
            i += 1
        result[key] = row
    
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Selects column user cares about."""
    result: dict[str, list[str]] = {}

    for column in columns:
        result[column] = table[column]
    
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatinates two tables into a singular one."""
    result: dict[str, list[str]] = {}

    for key in table1:
        result[key] = table1[key]

    for key in table2:
        if key in result:
            result[key] += table2[key]
        else:
            result[key] = table2[key]
    
    return result


def count(list1: list[str]) -> dict[str, int]:
    """Counts the number of times an element appears in a list."""
    if len(list1) == 0:
        raise ("Empty list passed throught")
    elif len(list1) == 1:
        return {list1[0]: 1}
    else:
        result: dict[str, int] = {}
        for string in list1:
            if string in result:
                result[string] += 1
            else:
                result[string] = 1
        
        return result