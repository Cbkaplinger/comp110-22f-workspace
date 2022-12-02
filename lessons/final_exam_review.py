"""Review for the final exam."""

def reverse_multiply(initial: list[int]) -> list[int]:
    final: list[int] = []
    reverse_index: int = len(initial) - 1

    for _ in initial:
        final.append(initial[reverse_index] * 2)
        reverse_index -= 1

    return final


def free_biscuits(d: dict[str, list[int]]) -> dict[str, bool]:
    new_dict: dict[str, bool] = {}

    for game in d:
        points: int = 0
        for value in d[game]:
            points += value

        if points >= 100:
            new_dict[game] = True
        else:
            new_dict[game] = False

    return new_dict


def multiples(initial: list[int]) -> list[bool]:
    result: list[bool] = []
    index: int = 0

    if initial[len(initial) - 1] % initial[index] == 0:
        result.append(True)
    else:
        result.append(False)

    while index < len(initial) - 1:
        if initial[index + 1] % initial[index] == 0:
            result.append(True)
        else:
            result.append(False)
        index += 1
    
    return result


def merge_lists(lhs: list[str], rhs: list[int]) -> dict[str, int]:
    merged_list: dict[str, int] = {}
    index: int = 0

    if len(lhs) != len(rhs):
        return merged_list

    for _ in lhs:
        merged_list[lhs[index]] = rhs[index]
        index += 1

    return merged_list


def reverse_string(initial: str) -> str:
    new_string: str = ""
    index: int = len(initial) - 1

    for _ in initial:
        new_string += initial[index]
        index -= 1

    return new_string


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int):
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int):
        self.marshmallow_count += mallows
        self.sweetness += mallows * 2
    
    def calorie_count(self) -> float:
        total_cals: float = 0.0

        if self.flavor == "vanilla" or self.flavor == "peppermint":
            total_cals += 30
        else:
            total_cals += 20

        if self.has_whip == True:
            total_cals += 100

        total_cals *= (self.marshmallow_count/2)

        return total_cals

class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, increase: int) -> None:
        self.minutes += increase

    def reset(self) -> int:
        old_minutes: int = self.minutes
        self.minutes = 0
        return old_minutes

    def report(self) -> None:
        time_in_hours: int = self.minutes // 60
        time_in_minutes: int = self.minutes % 60
        print(f"{self.name} has spent {time_in_hours} and {time_in_minutes} on {self.purpose}.")


def factorial(number: int) -> int:
    total: int = 1

    while number > 0:
        total *= number
        number -= 1
        factorial(number)

    return total



reverse_multiply([1, 2, 3, 4])
free_biscuits({"UNCvsDuke": [38, 20, 42] , "UNCvsState": [9, 51, 16, 23]})
multiples([2, 3, 4, 8, 16, 2, 4, 2])
merge_lists(["a", "b", "c"], [1, 2, 3])
reverse_string("abcdefg")

#x = HotCocoa(True, "vanilla", 12, 43)
#y = print(x.calorie_count())

#x = TimeSpent("Cameron", "time", 69)
#y = x.report()

print(factorial(0))