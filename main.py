def add(x=-1, y=-1, z=-1):
    """addd the values of x, y, and z.

    Args:
        x (numeric, optional): _description_. Defaults to -1.
        y (numeric, optional): _description_. Defaults to -1.
        z (numeric, optional): _description_. Defaults to -1.

    Returns:
        numeric: the addition of the values of x, y and z.
    """
    return x+y+z

if __name__ == "__main__":
    print(f"{add() = }")