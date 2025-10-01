# This code will raise error
"""
class NegativeNumberError(Exception):
    pass

def calculate_square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return x ** 0.5

try:
    result = calculate_square_root(-9)
    print("Square root:", result)
except NegativeNumberError as e:
    raise ValueError("Invalid input") from e
"""
# When we change -9 with 9

class NegativeNumberError(Exception):
    pass

def calculate_square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return x ** 0.5

try:
    result = calculate_square_root(9)
    print("Square root:", result)
except NegativeNumberError as e:
    raise ValueError("Invalid input") from e
