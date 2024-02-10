"""
We need to handle exceptions raised from a small chunk of code.
We are not going to cover 500 lines of code to be handled under one exception handling.
If we do that, then it will be hard to find exactly where its happened.
Try to handle/catch very specific exceptions not the broad ones (such as Exception).

"""

try:
    1 / 0
except ZeroDivisionError as ex:
    print(f'Exception occurred: {type(ex)}, {ex}')
print("Code continue running here ...")

# "Look before you leap" approach
l = [1, 2, 3, 4, 5]

while len(l) > 0:
    print(l.pop())
print("All done")

# We can avoid using the len() checking for each step using exception handling.
# This is means "Easier to ask forgiveness than permission"
l = [1, 2, 3, 4, 5]
try:
    while True:
        print(l.pop())
except IndexError as ex:
    # IndexError happened
    print("All Done")

# We can use "Exception" or "LookupError" to catch the exception but it will be broad.
# Also KeyError is derived from LookupError. So its hard to tell which one exactly
# happened. So using specific exception is always recommended.

# Multiple exception handling (using nested try-except)
data = [1, 2, 3, 4, 'abc']  # 'abc' will cause TypeError
sum_up = 0
count = 0

try:
    for d in data:
        try:
            sum_up += d  # Type error will happen here
            count += 1
        except TypeError:
            pass  # Basically skip (no-op)
    average = sum_up / count
except ZeroDivisionError:
    average = 0

print(f"Average: {average}")

# We can use broad exception catching, if we log the details somewhere.
try:
    1 / 0
except Exception as ex:
    print(f"looging error: {ex}")  # we can use python logging module
    # raise # we can raise the same exception without explicitly mention it
print("program still running")

# Finally statement

try:
    raise ValueError("Raised from the try block")
except ValueError as ex:
    print(f"Exception handled/logged: {ex}")
    raise TypeError("This is type error")  # Even though finally will execute
    # Traceback/stacktrace will show the chain of exception raise. So we can see thw root cause
finally:
    print("This will always executed")
print("Done")
