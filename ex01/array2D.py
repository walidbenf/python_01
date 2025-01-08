def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array and returns a truncated version based on start and end.
    Prints the shape before and after slicing.

    Args:
        family: 2D list of numbers
        start: starting index for slicing
        end: ending index for slicing

    Returns:
        Sliced 2D list
    """
    # Validate input is a list
    if not isinstance(family, list):
        raise ValueError("Input must be a list")

    # Validate family is non-empty
    if not family or not all(isinstance(row, list) for row in family):
        raise ValueError("Input must be a non-empty 2D list")

    # Validate all rows have same length
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All rows must have the same length")

    # Print original shape
    print(f"My shape is : ({len(family)}, {row_length})")

    # Slice the array
    result = family[start:end]

    # Print new shape
    print(f"My new shape is : ({len(result)}, {row_length})")

    return result
