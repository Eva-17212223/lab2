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

