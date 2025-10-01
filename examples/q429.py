def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Traceback information:")
        print(e.__traceback__)
        raise ValueError("Cannot divide by zero") from e
    return result

try:
    result = divide_numbers(5, 0)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)
