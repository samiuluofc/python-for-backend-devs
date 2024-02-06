"""
Comprehension means "easy way to create a new iterable from another iterable".
Similar to for loop, but easier and more concise syntax.

However, it works well with simple cases. Complex cases are possible, but it quickly become
un-readable. Readability matters, so in that case regular for/while loop is recommended.

Comprehensions are actually functions.
*   new_iterable = [ expression for item in iterable]
*   new_iterable = [ expression1 for item in iterable if expression2] # if expression2 if false it skip the loop step.

Different types of Comprehensions:
* List comprehensions
* Dict comprehensions
* Set comprehensions


Comprehension is slightly faster than regular looping. However, its insignificant.
"""
from math import sqrt
from time import perf_counter

# Time comparison

# Regular looping
start = perf_counter()
sqrt_list = []
for n in range(10_000_000):  # first 10 million numbers
    sqrt_list.append(sqrt(n))
print(len(sqrt_list))
elapsed_time = perf_counter() - start

print(f"Time for regular looping: {elapsed_time:.4f} seconds")

# list comprehension
start = perf_counter()
sqrt_list = [n**2 for n in range(10_000_000)]
print(len(sqrt_list))
elapsed_time = perf_counter() - start

print(f"Time for comprehension: {elapsed_time:.4f} seconds")
