"""
Decorators are a form of meta-programming (modify how some piece of code runs by using another piece of code).

Decorators allows us to wrap functionality around an already defined functionality (Simple extension of closure).

THat means its actually decorate any existing function.

Decorator leverages following things:
* Closure
* higher order function
* re-assign any object (such as function) to an existing symbol/variable

Example usage:
* Add logging functionality to all existing functions
* Reduce code repetition (less headache to manage). DRY: Dont Repeat Yourself
* Decorators are handy for adding pre and post function call code

Basic decorator pattern:

def wrapper(fn):
    def inner(*args, **kwargs):
        # Some extra code
        result = fn(*args, **kwargs)
        # Some extra code
        return result
    return inner

def add(a, b):
    return a + b

add = wrapper(add) # Re-assign

So this re-assign can be done through a shorthand notation:

@wrapper # basically just doing this: add = wrapper(add)
def add(a, b):
    return a + b
"""

from time import perf_counter


def log(func):

    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(
            f"INFO: Called {func.__name__} function. Elapsed time: {end - start}"
        )
        return result

    return inner


@log  # This is actually doing just 'add = wrapper(add)'
def add(a, b, c):
    return a + b + c


@log  # This is actually doing just 'mul = wrapper(mul)'
def mul(a, b):
    return a * b


@log
def greet(name):  # This is actually doing just 'greet = wrapper(greet)'
    return f"Hello {name}"


res1 = add(1, 2, 3)
res2 = mul(3, 7)
res3 = greet("Samiul")
print(res1, res2, res3)
