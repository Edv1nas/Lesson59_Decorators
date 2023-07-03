import functools


# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
#     return decorator_repeat


# """def say_whee():
#     print("whee")


# say_whee = repeat(5)(say_whee)

# say_whee()"""

# """or"""


# @repeat(5)
# def say_whee():
#     print("whee")


# say_whee()

"""Ex2"""


# def repeat(_func=None, *, num_times=2):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat

#     if _func is None:
#         return decorator_repeat
#     else:
#         return decorator_repeat(_func)


# @repeat
# def say_whee():
#     print("Whee!")


# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")


# greet("lapas")

"""Ex3"""


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 10
    return wrapper_count_calls


@count_calls
def say_whee():
    print("Whee!")


say_whee()
say_whee()
say_whee.num_calls
