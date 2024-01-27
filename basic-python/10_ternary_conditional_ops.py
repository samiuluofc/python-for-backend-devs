"""
Ternary conditional operator
var = value1 if <some_condition> else value2
var = expression1 if <some_condition> else expression2

Also it follow the short-circuited evaluation. Between expression1 and expression2
it executes only one of them depending on the condition.

Definitely the same thing is possible with if-else, but this improves the readability (like english language).

Useful to replace simple regular if-else.
"""

a = 10
b = 20
var1 = a if a > b else b
print(var1)
var2 = (a - b) if a > b else (b - a)
print(var2)
