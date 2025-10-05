def safe_divide(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    return f"The result of the division is: {result}"