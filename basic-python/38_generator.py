"""
We have seen list, dict and set comprehension.
But no tuple comprehension, cause its not mutable, tuple has no append function.

But wee can right this expression: (i ** 2 for i in range(5)).
Its actually a generator object.
Generators are iterators.
Generators calculate each element one by one upon request using next function.
Generators implements next method.
Generators use lazy iteration (lazy property is the one that is not calculated until its requested.)
Generators are one time use thing like regular iterators.
Generators are used for memory efficiency.
*   For example, we can read one line at a time from a file, process it, return the result, discard it,
and then pick the next line. We dont need to have the whole file at a time in a memory.

Downside:
* They are one time use. Data/iterables stays in the memory to process again.
* You dont have the whole sequence at a time.

Two ways to create generators:
1. Using generator comprehension using '()'
2. Using yield (instead of return we are yield from a function)

"""
from timeit import timeit

squares = [i**2 for i in range(6)]  # list comprehension
print(type(squares), squares)

squares = (i**2 for i in range(6))  # generator
print(type(squares))  # generator class

print(next(squares))

try:
    while True:
        element = next(squares)
        print(element)
except StopIteration:
    pass

for i in squares:
    print(i)  # Nothing will be printed, cause its already iterated

# Need to recreate the generator
squares = (i**2 for i in range(6))  # generator
for i in squares:
    print(i)

print(iter(squares) is squares)  # generators are iterator

# generators cannot be used twice
squares = (i**2 for i in range(6))  # generator
print(list(squares))
print(list(squares))  # already used fully in the previous line

# Can be partially used
squares = (i**2 for i in range(6))  # generator
print(9 in squares)
# It has been used upto index 3 (9 in this case), to find it.
print(list(squares))  # showing the remaining

# Compare list comprehension vs generator

elapsed_time = timeit('[i ** 2 for i in range(25_000_000)]', number=1)
print(elapsed_time)

elapsed_time = timeit('(i ** 2 for i in range(250_000_000_000))', number=1)
print(elapsed_time)
# The above one actually does not even depends on the size of the data,
# cause it will create the number once its requested.

# Its memory efficient if we can process one element at a time.
# its faster if we dont need to traverse through all numbers.
