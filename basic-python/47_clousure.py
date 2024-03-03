"""
What is closure:
* A function can define inside another function (called outer function and inner function)
* All the variables (parameters and local variables) of outer functions are accessible to the inner function
* Even after returning the inner function (when outer function is all done), the inner function actually remembers the variables of the outer function
* So the inner function is not a simple function, it can also "captures" the variables of the outer function.
* That is why this special inner function is called closure.


Why its needed:
Python has a useful feature called 'Decorator', which use the concept of closure.

"""
from time import perf_counter


def outer(a, b):
    sum_ = a + b

    # This is closure because its using a, b and sum_ from outer function.
    # Note: if inner does not use anything from the outer function, its not a closure
    def inner(n):
        prod = a * b * n
        print(a, b, sum_, prod)

    return inner


my_func = outer(10, 10)
my_func(12)
print(my_func.__closure__)  # It remembers a, b and sum_


# Another example: function generator
def power(n):

    def inner(x):
        return x**n

    return inner


square = power(2)
cube = power(3)
print(square(10))
print(cube(10))


# Another example: execute function
def executor(func):

    def inner(*args,
              **kwargs):  # variable length positional and keyword arguments
        result = func(*args, **kwargs)  # unpacking
        return result

    return inner


def add(a, b, c):
    return a + b + c


def multi(a, b, c, d):
    return a * b * c * d


def say_hello(name):
    return f"Hello {name}."


my_adder = executor(add)
my_multiplier = executor(multi)
my_greeting = executor(say_hello)
print(my_adder(10, 20, 30))
print(my_multiplier(1, 2, 3, 4))
print(my_greeting("Samiul"))

# An example similar to Decorator.
# Calculate execution time for any function


def factorial(n):
    mul = 1
    for i in range(n):
        mul = mul * (i + 1)
    return mul


def diagonal_matrix(size, *, diagonal=1):
    return [[diagonal if row == col else 0 for col in range(size)]
            for row in range(size)]


def time_it(func):

    def inner(*args, **kwargs):
        start = perf_counter()  # wrapped the timing code
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Duration: {end - start}")
        return result

    return inner


print(factorial(5))
print(diagonal_matrix(5, diagonal=1))

factorial_with_time = time_it(factorial)
diagonal_matrix_with_time = time_it(diagonal_matrix)

print(factorial_with_time(5))
print(diagonal_matrix_with_time(5))
