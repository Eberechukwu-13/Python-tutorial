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


def str_find(
    sub: str,
    string: str,
    start: int | None = 0,
    end: int | None = None,
) -> int:
    """Find the index of substring 'sub' in text 'string'.

    Args:
        sub (str): substring to search in 'string'.
        string (str): text to search substring 'sub'.
        start (int | None, optional): begine at this given ihdex position to search. Defaults to 0.
        end (int | None, optional): stop search at this given index position. Defaults to None.

    Returns:
        int: index of the substring 'sub'.

    """
    return string.find(sub, start, end)
