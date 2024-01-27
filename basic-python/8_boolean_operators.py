"""
Two boolean values: True, False
Boolean operators: and, or and not.
Need to know the Truth table for and, or and not.

(A and B), for python if expression A is false, it will immediately
return False. Saving time to calculate expression B. This called
'short-circuited' evaluation. So remember to place less costly expression
in the place of A.

This is same for (A or B). If A is True, python will ignore B.
"""

print(not True)
print(True and False)
print(True or False)

limit = 500.0
withdraw = 5000.0
balance = 1000

if (withdraw <= limit) and (withdraw <= balance):
    print(f"You are allowed to withdraw {withdraw}")
else:
    print(f"You are NOT allowed to withdraw {withdraw}")

a = 20
b = 0

print(b != 0 and (a / b) > 1)
# instead of ZeroDivisionError, its False. Because
# short circuited evaluation only executed b != 0 first, which is False in this case.
# So its never executes the second part (a / b).
