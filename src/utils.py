#add function:

def add(*args):
    return sum(*args)


#Substract function:
def subtract(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    if not args:
        return None
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero")
        result /= num
    return result
