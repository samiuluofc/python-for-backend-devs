"""
Filtering is a selection of a subset of items based on whether some condition is true or false
For example: Given a list of numbers from 1 to 100, filter this list to contain even numbers only.

We need to apply the predicate function (for example is_even function) on every element in the
list. Keep the elements where predicate function returns True.

A predicate function is simple a function that takes one or more arguments and returns True or False.

For filtering in general:
* given a predicate function and an iterable
* only keep the items for which predicate function evaluates to True (generates a new iterable)

Python has builtin filter function:
    filter(predicate, iterable)
    Returns an iterator (Need to iterate through to get the result)
"""

data = [1, 3, 4, 5, 2, 3, 10, 11]


def is_odd(num):
    if num % 2 == 1:
        return True
    return False


iterator = filter(is_odd, data)  # Lazy filter
print(type(iterator))
print(list(iterator))

# More example:
# Given two lists keep those numbers where sum of two numbers at index i is even
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = [3, 1, 3, 4, 50, 61, 9, 23]
print(list_1)
print(list_2)

zipped_list = zip(list_1, list_2)


def is_even(t):
    if (t[0] + t[1]) % 2 == 0:
        return True


result = list(filter(is_even, zipped_list))

# This is equivalent to calling zip with each element of the list as a separate argument
t1, t2 = zip(*result)
list_1 = list(t1)
list_2 = list(t2)
print(list_1)
print(list_2)
