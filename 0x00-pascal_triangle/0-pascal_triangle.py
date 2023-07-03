def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.

    Raises:
        None

    Notes:
        - If n is less than or equal to 0, an empty list is returned.
        - The function assumes n will always be an integer.
    """

    pascalt = []

    if n <= 0:
        return pascalt

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                value = pascalt[i - 1][j - 1] + pascalt[i - 1][j]
                row.append(value)
        pascalt.append(row)

    return pascalt
