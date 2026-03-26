def add(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Can not add not int variables"


result: int = add(2, "3")
