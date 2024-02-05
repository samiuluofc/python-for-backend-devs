"""
Break means exit from the loop immediately.
Continue means go back to beginning of the loop immediately.
Works for both 'for' and 'while' loop.
Else statement can be used with 'for' and 'while' loop.
Else part will be executed if for/while loop never encountered a break statement.
"""

for i in range(300):
    print(i)
    if i > 10:
        print("Breaking out of the loops")
        break
print("Done!")

for i in range(30):
    if i % 2 == 0:
        continue  # want skip next statements/codes for even numbers
    print(i)  # print odd numbers only
print("Done!")

# Write a program to find all numbers in a list is positive or not.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
all_positive = True

for ele in data:
    if ele < 0:
        all_positive = False  # one violates the condition, so break immediately
        break
if all_positive:
    print("All positive numbers")

data = [1, 2, 3, 4, 5, -6, 7, 8, 9]
# Basically in the above program we are trying to figure out the 'break' statement was executed or not.
# To do that we have used the flag. However, python has 'else' with for loop to tackle that.
# Else will be executed, if 'for' has encountered no 'break' (executed all steps of loop).
# Following approach does not need the flag anymore.
for ele in data:
    if ele < 0:
        break
else:
    print("All positive numbers")
