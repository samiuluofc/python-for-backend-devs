"""
Unpacking sequences (list, tuple and string).
LHS (left hand side) and RHS (right hand side) should have same number of elements.
Useful to return multiple returns from function.
"""

a, b, c = (10, 20, 30)  # Tuple
print(a, b, c)

a, b, c = 1, 2, 3  # Tuple (Dont need the braces actually)
print(a, b, c)

a, b, c = [100, 200, 300]  # List
print(a, b, c)

a, b, c = 'xyz'  # string
print(a, b, c)

a = 10
b = 20
c = 30
a, b, c = a + b, b + c, c + a
print(a, b, c)

# Swap two variables
a = 12
b = 13

print(a, b)
temp = b
b = a
a = temp
print(a, b)

# Easy Swap with unpacking
a, b = b, a
# Python evaluates RHS first, so it creates the tuple (b, a) first then assign them to a, b.
print(a, b)


def my_func(a, b):
    return a + b, abs(b - a)  # multiple returns as Tuple


m, n = my_func(30, 40)
print(m, n)
