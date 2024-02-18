# Anonymous function (does not have a name)
# They do not have a code block (it must me a single statement/expression that will be executed and returned)
# No need to use explicit return.

# The expression "lambda para1, para2,.. : <single expression using parameters>" returns as a function object
# Lambda is useful as simple and short lived functions (using it for single time, such as passing as a parameter into another function)

f = lambda a, b: a + b
print(f(1, 3))  # However, no need to use lambda function as regular function
print(type(f))


# This is a single expression regular function (can be a lambda)
def identity(rows, cols):
    return [[1 if row == col else 0 for col in range(cols)]
            for row in range(rows)]


print(identity(5, 9))

# We can use default arguments or *args or **kwargs
f = lambda rows=1, cols=1: [[1 if row == col else 0 for col in range(cols)]
                            for row in range(rows)]

print(f(5, 9))  # not necessarily use lambda function in this scenario
print(f())
# Use lambda when it make sense (suppose a short lived function object as parameter to another function)

# It sometimes hard to debug with a function without name :(
