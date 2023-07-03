"""
1. create a function that adds as many numbers as are being passed to it.
2. create another one that multiplies as many numbers as are being passed to it.
3. create a decorator that creates a file and appends arguments and a result to the file.
"""


def append_result_to_file(file_name):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            with open(file_name, 'a') as file:
                arguments = ', '.join(str(arg) for arg in args)
                file.write(f"Arguments: {arguments}\n")
                file.write(f"Result: {result}\n")
            return result
        return wrapper
    return decorator


@append_result_to_file('result_of_sum.txt')
def add_numbers(*args):
    return f"Sum of added numbers: {sum(args)}"


@append_result_to_file('result_of_multiplication.txt')
def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return f"Multiplication: {result}"


input_numbers = input(
    "Please add number for function add and multiply (separeted by spaces): ").split()
numbers_list = [int(num) for num in input_numbers]

adds = add_numbers(*numbers_list)

multi = multiply_numbers(*numbers_list)
