"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730570002"


class Simpy:
    """Manual functions that simulate the NumPy package."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the attributes of the list."""
        self.values = values

    def __repr__(self) -> str:
        """Converts the list into a string."""
        return f"Simpy({self.values})"

    def fill(self, fill_value: float, number_of_val: int) -> None:
        """Fills the list with a given float value and number of values that make up the list."""
        self.values = []
        for _ in range(number_of_val):
            self.values.append(fill_value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the list with a range of values when given starting and ending numbers and a step size."""
        assert step != 0.0

        while start < stop:
            self.values.append(start)
            start += step
        else:
            while stop < start:
                self.values.append(start)
                start += step
        
    def sum(self) -> float:
        """Adds all the values in the list together."""
        total: float = 0
        index: int = 0

        for _ in range(len(self.values)):
            total += self.values[index]
            index += 1
        
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds two lists together and outputs one list."""
        result: Simpy = Simpy([])
        
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
                
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raises the first list to the power of the second list and outputs one list."""
        result: Simpy = Simpy([])
        
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
                
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a boolean list of whether the indexes of list1 and list2 are equal."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for item in range(len(self.values)):
                if self.values[item] == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for index in range(len(self.values)):
                if self.values[index] == rhs.values[index]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a boolean list of whether the indexes of list1 is greater than list2."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for item in range(len(self.values)):
                if self.values[item] > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for index in range(len(self.values)):
                if self.values[index] > rhs.values[index]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns the subscript operator with Simpy opbjects. Also uses the __getitem__ method to do the subscription notation."""
        bool_list: list[bool] = []
        simpy_list: Simpy = Simpy([])

        if isinstance(rhs, int):
            for item in range(len(self.values)):
                if self.values[item] == rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)

            for item in range(len(bool_list)):
                if bool_list[item] is True:
                    simpy_list.values.append(self.values[item])
            
            result: float = 0.0
            result = self.values[rhs]          
            return result
        else:
            for item in range(len(self.values)):
                if rhs[item] is True:
                    simpy_list.values.append(self.values[item])
            
        return simpy_list