"""
write a decorator that checks if the output of the function in a positive integer, 
if it is not print "RESULT IS NEGATIVE" otherwise print "RESULT IS POSITIVE
""""

def positive_integer_check(func):
    def integer_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int and result > 0:
            print("RESULT IS POSITIVE")
        else:
            print("RESULT IS NEGATIVE")
        return result
    return integer_wrapper


@positive_integer_check
def add(a, b):
    return a + b


@positive_integer_check
def multiply(a, b):
    return a * b


@positive_integer_check
def subtraction(a, b):
    return a - b


@positive_integer_check
def some_number(a):
    return a


result1 = add(1, 2)
result2 = multiply(1, 2)
result3 = subtraction(-5, 2)
result4 = some_number(-2)
