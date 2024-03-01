"""
Functions are object as well.
Functions can be returned or pass as a parameter.
Higher order function: A function that can take another function as parameter or can return another function.

A function definition can be inside another function. In other word functions can be nested.
Inner function has access to all parameters of outer function.

Passing or returning a function: function name without '()'.

Function body can contain any valid python code such as another function/class.

Its very common in python to have a function definition inside a function and return the inner function from it.
"""
from time import perf_counter

# Passing function to another function


def add(a, b):
    return a + b


def greet(name):
    return f"Hello {name}"


res1, res2 = add(5, 6), greet("Samiul")
print(res1, res2)


def apply(func, *args):
    res = func(*args)  # unpacking the args
    return res


# passing function as argument
print(apply(add, 5, 6), apply(greet, "Samiul"))

# We can send a lambda function as well
print(apply(lambda a, b, c: a + b + c, 10, 20, 30))


# Returning a function from another function
def choose_operator(name):

    def multi(a, b):
        return a * b

    def power(a, n):
        return a**n

    if name == 'multi':
        return multi
    if name == 'power':
        return power


op = choose_operator('power')
print(op, op(2, 10))


# We could return lambda function as well instead of define the regular function
def choose_operator_with_lambda(name):
    if name == 'multi':
        return lambda a, b: a * b
    if name == 'power':
        return lambda a, n: a**n


op = choose_operator('power')
print(op, op(2, 10))

# Another example


def in_list(l, element):
    return element in l


def in_tuple(t, element):
    return element in t


def in_set(s, element):
    return element in s


def time_it(func, *args):
    start = perf_counter()
    res = func(*args)
    end = perf_counter()
    print(end - start)
    return res


x = 5_000_000
n = 10_000_000
l = list(range(n))
t = tuple(range(n))
s = set(range(n))

time_it(in_list, l, x)
time_it(in_tuple, t, x)
time_it(in_set, s, x)  # Fastest to find x
