import functools
#decorators

# def mydecorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @mydecorator
# def func():
#     pass
#_----------------------------------------------
# def start_end_decorator(func):#func for the inner function

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# @start_end_decorator
# def print_name(x):
#     print('jugu :)')

# print(help(print_name))
# print_name(print_name.__name__)

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')
greet('jugu')