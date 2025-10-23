# Add function:
def add(*args):
    return sum(args) if args else 0


# Substract function:
def subtract(*args):
    if not args:
        return 0
    result = args[0]
    for n in args[1:]:
        result -= n
    return result


# Multiply function:
def multiply(*args):
    if not args:
        return 0
    result = 1
    for n in args:
        result *= n
    return result


# Divide function:
def divide(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result /= num
    return result
