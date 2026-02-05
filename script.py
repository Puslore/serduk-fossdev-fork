def sum(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator couldn't be a zero")
    if isinstance(a, str) or isinstance(b, str):
	    raise ValueError("Divisors couldn't be a string")
<<<<<<< HEAD
    return a / b
=======
    return a / b
>>>>>>> fix/missing-test
