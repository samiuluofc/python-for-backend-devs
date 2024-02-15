"""
Why functions:
1. Easy code reuse
2. breaking up complex code to easily understandable chunks

When we DEFINE a function we define variables (inputs) that will be passed to the functions.
These are called parameters.

When we CALL a function, we pass the values for those parameters.
These are called arguments.

Just like everything in python, function is an object too.
They are callable.
They always return something (at least None).
They can be assigned to a variable/symbol.
They can be pass to another function.
They can be return from another function.


Callable:
An object is callable if it can be called using '()'
Example:
    print('Hello')

Positional arguments: Arguments are assigned to its corresponding variables/parameters based on position.

Functions does not stay/hold any memory, function runs within its own local namespace (a dictionary that
contains all the variables and its value). Once the function is done it deletes everything (remove the dictionary).
They always starts fresh, execute some code, return the result and removes everything.
Consecutive call of same functions are independent of each other.

"""
from datetime import datetime


def custom_func():
    print('Hello')


a = custom_func
print(type(a), a)

b = 100_000
ret = a()
print(type(ret), ret)  # None is also an object

print(globals())  # Global namespace is actually a dictionary
print(globals()['custom_func'])
print(globals()['b'])

# function is an object, it has properties as well
print(a.__name__, custom_func.__name__)

# function parameters and arguments


def add(a, b, c):  # parameters
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    sum_ = a + b + c  # sum is a built in function, so use _ to differentiate it
    print("local variables inside function", locals())
    return sum_


result = add(5, 6, 7)
print(result)
result = add(100, 200,
             300)  # local is always recreated when a function is called
print(print)


# no return (actually returns None)
def log(message):
    dt = datetime.utcnow().isoformat()
    print(f"{dt} - [message]")
    # no return


result = log("Log 1")
print(result)


# bail out from a function
def is_all_positive(data):  # We can send any iterables as argument
    for element in data:
        if element < 0:
            return False
    return True


list_of_numbers = [1, 2, 3, 4, -5, 6]
print(is_all_positive(list_of_numbers))
list_of_numbers = [1, 2, 3, 4, 5, 6]
print(is_all_positive(list_of_numbers))
print(is_all_positive(range(1, 10)))
print(is_all_positive(range(1, -10, -2)))
d = {'a': 1, 'b': 2, 'c': 3}
print(is_all_positive(d.values()))


# Named and positional arguments
def gen_matrix(rows, cols, default_value):
    return [[default_value for _ in range(cols)] for _ in range(rows)]


print(gen_matrix(4, 8, 1))  # positional arguments
print(gen_matrix(
    cols=8, rows=4,
    default_value=1))  # Named arguments, no need to worry about the order

# Note: once you start using named arguments, you no longer use the positional ones.
# In short, all positional arguments are at the beginning and then all the named ones.
# However, mixing them is not a good practice
