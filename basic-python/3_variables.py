"""
Label objects with a name, so that we can use same object in multiple parts of a code.
Use single assignment operator to assign a value to a variable.

Variable naming rules:
1. case sensitive
2. must starts with _ or letters (a - z, A - Z)
3. Cannot start a variable with digits
4. Cannot use reserved words (part of python language) as variable names


Python style guide (PEP8): https://peps.python.org/pep-0008/
YAPF pre-commit-hook is following PEP8.
Google python style guide: https://google.github.io/styleguide/pyguide.html

Variable names should use snake_case in python: multi_words_separated_by_underscore_all_lower_case.
CamelCase for class names and Exceptions.
Give variables meaningful names (multi words, its more readable). Single character is not recommended.
"""

account_balance = 1000.00  # reference to the float object 1000.00

# left-hand-side (LHS) = right-hand-side (RHS). Python evaluates RHS first.
balance = 1000.50 - 200.50
print(balance)

# operator and operand.
a = 10
b = 20
c = a + b  # here a, b and c are operands and '+' and '=' are operators.

# if = 5, we cannot do this cause its reserved keyword
a = float(10)
print(type(float))
float = 100  # we can do this but its a bad approach. Be careful, do not override builtin functions/class
print(type(float))
