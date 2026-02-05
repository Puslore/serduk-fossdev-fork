def sum(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator couldn't be a zero)
    return a / b