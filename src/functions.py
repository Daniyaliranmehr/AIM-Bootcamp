def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2

def power(base, exponent):
    if base == 0 and exponent < 0:
        return "Error! Zero cannot be raised to a negative power."
    return base ** exponent
