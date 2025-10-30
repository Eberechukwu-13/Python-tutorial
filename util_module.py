"""Utility functions."""


def str_count(
    string: str,
    sub: str,
    start: int | None = None,
    end: int | None = None,
) -> int:
    """Count the number(s) of substring 'sub' in text 'string'.

    Args:
        string (str): text to count substring 'sub'.
        sub (str): substring to count in string.
        start (int | None, optional): start at this given index position. Defaults to None.
        end (int | None, optional): stop at this given indec position. Defaults to None.

    Returns:
        int: the number of occurance of sub string 'sub' in string.

    """
    return string.count(sub, start, end)
