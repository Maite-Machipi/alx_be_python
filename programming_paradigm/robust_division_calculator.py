# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two values, handling non-numeric input and division by zero.

    Returns:
        - "The result of the division is X" on success
        - "Error: Cannot divide by zero." if denominator is zero
        - "Error: Please enter numeric values only." if inputs are not numbers
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
