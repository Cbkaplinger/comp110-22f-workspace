"""Example of a class and object instantiation."""

class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool = False


    def __init__(self, size: str, toppings: int):
        """Constructor definiton for initialization of attributes."""
        self.size = size
        self.toppings = toppings


    def price(self, tax: float) -> float:
        total: float = 0.0

        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total

pizza1: Pizza = Pizza("large", 3)
pizza1.size = "large"
pizza1.toppings = 3

pizza2: Pizza = Pizza("small", 0)
pizza2.extra_cheese = True

print(Pizza)

print(pizza1)
print(pizza1.size)
print(f"Price: ${pizza1.price(1.05)}")

print(pizza2.size)
print(f"Price: ${pizza2.price(1.05)}")