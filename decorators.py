"""Ex1"""

# def parent(num):
#     def first_child(name):
#         return f"Hi, I am {name}"

#     def second_child(name):
#         return f"Call me {name}"

#     if num == 1:
#         return first_child
#     else:
#         return second_child


# # Call the parent function with an argument
# result = parent(1)

# # Call the returned function with the name argument
# print(result("Emma"))

"""Ex2"""

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper


# def say_whee():
#     print("Whee!")


# say_whee = my_decorator(say_whee)

"""Ex3"""


# from datetime import datetime
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper


# def say_whee():
#     print("Whee!")


# say_whee = not_during_the_night(say_whee)
# say_whee()

"""Ex4"""


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper


# @my_decorator
# def say_whee():
#     print("Whee!")

"""Ex5"""

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice


# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"


# greeting = return_greeting("Lapas")
# print(greeting)

"""Ex6"""




import functools
import time
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(1000000)])


print(waste_some_time(1000000))
