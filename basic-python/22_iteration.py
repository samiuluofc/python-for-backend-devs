"""
Repetition is called iteration. We iterate over elements of some container such that sequences.
More generally over objects that iterable.

Not all iterables are sequences (suppose a set of marbles).

Deterministic iteration (For loop)
Non-deterministic iteration (While loop)


range object is an iterable object on integer.
* We can use the range() function to create a range object.
* It serves up integer one by one as you requested.
* Full range of integers does not exist at a time in the memory.
* Finite number of integers, thats why it used only with 'for' loop.

3 ways to use:
* range(end) # start is 0, step is 1
* range(start, end) # step is 1
* range(start, end, step)

Here end is excluded, which means (end - 1)
"""

r = range(5)
print(r, type(r), len(r))

# convert range object to a list or tuple to generate all the integers
print(list(r))
print(tuple(r))

print(list(range(3, 9)))
print(list(range(1, 20, 2)))  # all odd numbers
