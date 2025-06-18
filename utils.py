from typing import Union


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate and return the sum of two numbers.

    This function takes two numeric values (integers or floats) and returns
    their sum. The return type will be an integer if both inputs are integers,
    otherwise it will be a float.

    Args:
        a (Union[int, float]): The first number to add.
        b (Union[int, float]): The second number to add.

    Returns:
        Union[int, float]: The sum of a and b.

    Raises:
        TypeError: If either argument is not a number (int or float).

    Examples:
        >>> add_numbers(1, 2)
        3
        >>> add_numbers(1.5, 2.5)
        4.0
        >>> add_numbers(1, 2.5)
        3.5
    """
    # Input validation
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be a number (int or float), got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be a number (int or float), got {type(b).__name__}")

    return a + b


if __name__ == "__main__":
    # Test with integers
    print(f"add_numbers(1, 2) = {add_numbers(1, 2)}")

    # Test with floats
    print(f"add_numbers(1.5, 2.5) = {add_numbers(1.5, 2.5)}")

    # Test with mixed types (int and float)
    print(f"add_numbers(1, 2.5) = {add_numbers(1, 2.5)}")

    # Test with negative numbers
    print(f"add_numbers(-1, 3) = {add_numbers(-1, 3)}")

    # Demonstrate error handling for invalid input types
    print("\nTesting error handling:")
    try:
        result = add_numbers("1", 2)
        print(f"Unexpected success: {result}")
    except TypeError as e:
        print(f"Error caught as expected: {e}")

    try:
        result = add_numbers(1, None)
        print(f"Unexpected success: {result}")
    except TypeError as e:
        print(f"Error caught as expected: {e}")