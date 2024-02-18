"""
Keyword-only arguments: passing an arguments by
For example: def func(a, b, *args, c) # here c needs to pass as keyword arguments
How to do that:
1. add an *args parameter, which will make the rest of the parameter mandatory
For example: def func(a, b, *args, c, d) # here c and d needs to pass as keyword arguments (mandatory)
because python will be confused by the fact that which values from the args list will be goes to c and d.

"""


def func(a, b, *args, c, d):
    print(a, b, args, c, d)


# Will throw TypeError: func() missing 2 required keyword-only arguments: 'c' and 'd'
# func(1, 2, 3, 4, 5, 6, 7)

func(1, 2, 3, 4, 5, c=6, d=7)  # c and d is keyword only. So it worked


# but we dont want to allow unlimited number of args to pass to the func
# The solution is following
def func1(
    a,
    b,
    *,
    c=10,
    d
):  # Use a star only. This is not a variable. The parameter after that are keyword only
    print(a, b, c, d)


func1(1, 2, c=3, d=4)  # last two parameter has to be keyword-only

# SyntaxError: non-default argument 'c' follows default argument
# So that means if we define a default argument, we should also
# define it for the remaining arguments as well.
# Basically as parameters with default value should at the end of the
# parameter list
"""def my_func1(a, b=0, c, d=1):
    print(a, b, c, d)"""

# Arbitrary number of keyword-only parameters: **kwargs
# Full definition of a function parameters could be: func(a, b, *args, c, d, **kwargs)
# Here a and b are positional
# *args is arbitrary number of positional arguments (its a tuple)
# c and d are keyword-only arguments
#  **kwargs is arbitrary number of keyword-only arguments (its a dictionary).
# *args and **kwargs can be any name. But this two name is convention.


# Note: Use function doc string to describe its parameter
def func1(a, b, *args, c, d, **kwargs):
    """
    This is a function to do blah blah blah.
    a: parameter for ...
    b: ....

    This description will show in the VScode hover over description to a function
    """
    print(a, b, args, c, d, kwargs)


func1(1, 2, 3, 4, 5, c=10, d=20, e=4, f=5,
      g=4)  # here 'a' or 'b' with a default parameter is worthless

# Use *args or **kwargs only when it make sense. So use it when you really
# dont know (or dont need to know) what arguments are coming. Dont abuse it.

# Note: Use function doc string to describe its parameter
