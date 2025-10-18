"""Utility functions."""

from collections.abc import Sequence
from typing import overload

type Numeric = int | float | complex

type NumericOrSequence = Numeric | Sequence


@overload
def add() -> Numeric: ...
@overload
def add(arg1: Numeric, arg2: Numeric, arg3: Numeric) -> Numeric: ...
@overload
def add(arg1: Sequence, arg2: Sequence, arg3: Sequence) -> Sequence: ...
@overload
def add(
    arg1: NumericOrSequence,
    arg2: NumericOrSequence,
    arg3: NumericOrSequence,
) -> NumericOrSequence: ...


def add(arg1=-1, arg2=-1.1, arg3=-1j):
    """Add the values of arg1, arg2, and arg3.

    Args:
        arg1 (Numeric | Sequence): Defaults to -1.
        arg2 (Numeric | Sequence): Defaults to -1.1.
        arg3 (Numeric | Sequence): Defaults to -1j.

    Returns:
        Numeric | Sequence: the addition of the values of arg1, arg2 and arg3.

    """
    return arg1 + arg2 + arg3


if __name__ == "__main__":
    print(f"{add() = }")
