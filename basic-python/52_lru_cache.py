"""
For same set of parameters, if a function returns same outputs/returns then its a deterministic function.
Also if the function is costly and same set of parameters comes quite often then we can cache the function
using LRU cache decorator. This cache is in-memory cache.
It increase the speed of our code.

LRU means least recently used.
Cache should not grow indefinitely. It can store N most recent. if new results came in,
then it flashes the oldest one and add the new one.

The decorator is called @lru_cache(maxsize=100).
Restriction: arguments pass to a function must be hashable (immutable). Cannot be any list or dict.

"""

# Raw code solution
cache = {}


def add(a, b, c):
    key = (a, b, c)
    if key in cache:
        return cache[key]
    cache[key] = a + b + c
    return cache[key]


from functools import lru_cache


# This cache will grow unbounded
def cache(func):
    print("initialize the cache")
    cache_dict = {}

    def inner(*args):
        if args in cache_dict:
            print(f"Cache hit for {args}")
            return cache_dict[args]
        else:
            print(f"Cache miss for {args}")
            result = func(*args)
        cache_dict[args] = result
        return result

    return inner


@cache
def add(a, b, c):
    return a + b + c


@cache
def mul(a, b):
    return a * b


print(add(3, 5, 10))
print(add(3, 5, 10))
print(mul(3, 5))
print(mul(3, 5))


@lru_cache(maxsize=20)
def add_(a, b, c):
    print("Add function called")
    return a + b + c


@lru_cache(maxsize=20)
def mul_(a, b):
    print("Multi function called")
    return a * b


print(add_(3, 5, 10))
print(add_(3, 5, 10))
print(mul_(3, 5))
print(mul_(3, 5))

# Recursive fibonacci


def fibo(n):
    print(f"Called fibo({n})..")
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo(5))  # Repeated function calls
# To stop this repeated calls, we can cache the results
# This is called memoization.


@lru_cache(maxsize=3)
def f(n):
    print(f"Called fibo({n})..")
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)


print(f(5))  # No repetition
