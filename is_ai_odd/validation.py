"""
validation.py

Description:
    Provides functions to validate inputs before running core functions.
    Ensures that the data is of expected type integer
"""

def _valid(x: int) -> bool:
    """Returns a bool reflecting whether x is a valid integer or not

    Args:
        x (int): The value to be checked

    Returns:
        bool: Returns true if x is an integer
    """

    return isinstance(x, int)
