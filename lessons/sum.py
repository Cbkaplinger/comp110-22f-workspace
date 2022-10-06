"""Example of writing a test subject."""

def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    index: int = 0

    while index < len(xs):
        total += xs[index]
        index += 1
    return total