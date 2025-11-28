"""Utility functions."""

from collections.abc import Iterator, Sequence
from typing import overload

from util_module import str_count, str_find

type Numeric = int | float | complex


@overload
def add() -> Numeric: ...
@overload
def add(arg1: Numeric, arg2: Numeric, arg3: Numeric) -> Numeric: ...
@overload
def add(arg1: Sequence, arg2: Sequence, arg3: Sequence) -> Sequence: ...


def add(arg1=-1, arg2=-1.1, arg3=-1j):
    """Add the values of arg1, arg2, and arg3.

    Args:
        arg1 (NumericOrSequence): Defaults to -1.
        arg2 (NumericOrSequence): Defaults to -1.1.
        arg3 (NumericOrSequence): Defaults to -1j.

    Returns:
        NumericOrSequence: the addition of the values of arg1, arg2 and arg3.

    """
    return arg1 + arg2 + arg3


def find_substring(
    sub: str = "t",
    string: str = "i love python, git and github.",
    start: int | None = 0,
    end: int | None = None,
) -> Iterator[int]:
    """Find the index(es) of substring 'sub' in text 'string'.

    Args:
        sub (str): substring to search in 'string'. Defaults to "t".
        string (str): text to search substring 'sub'. Defaults to "i love python, git and github.".
        start (int | None, optional): begine at this given ihdex position to search. Defaults to 0.
        end (int | None, optional): stop search at this given index position. Defaults to None.

    Yields:
        Iterator[int]: index of the substring 'sub'.

    """
    count = str_count(sub, string, start, end)
    if not count:
        yield -1

    for _ in range(count):
        index = str_find(sub, string, start, end)
        yield index
        start = index + 1


if __name__ == "__main__":
    print(f"{add() = }")

    print(
        f"The indexes of the substring 'sub' in the text 'string' are: {list(find_substring())}",
    )
