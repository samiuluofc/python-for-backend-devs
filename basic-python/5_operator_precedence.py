"""
All python operators: https://python-reference.readthedocs.io/en/latest/docs/operators/

Best practice: Instead of relying on operator precedence, use parentheses to explicitly control the order of operations.

operator precedence: https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

print(100 + 200 - 50)  # '+' and '-' has same precedence
print(100 * 200 / 50)  # '*' and '/' has same precedence
print(2 * 10 + 6)  # its same as ((2 * 10) + 6)
print(2 * 2**2)  # its same as (2 * (2 ** 2))
print(-2**4)  # its same as -(2 ** 4), ** has higher precedence than unary -
print((-2)**4)  # now unary - is evaluated first
print(2**-2)  # However this is not -(2 ** 2), this is (2 ** (-2))
