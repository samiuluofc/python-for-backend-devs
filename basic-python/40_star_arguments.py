# *args means variable number of positional arguments
# Its not part of python syntax, its a convention to send N number of arguments

# We can use *args, *values, *numbers etc, just need parameter that has a '*' at the beginning
# That parameter will be a tuple.


def average(*args):
    print(type(args))
    print(len(args))
    return sum(args) / len(args)


res = average(1)
print("Result: ", res)
res = average(1, 3, 4)
print("Result: ", res)


def average1(a, b, *args):  # *arg takes in all the remaining arguments
    print(type(args))
    print(len(args))
    return (a + b + sum(args)) / (len(args) + 2)


res = average1(1, 10)  # a = 1, b = 10, arg = ()
print("Result: ", res)
res = average1(1, 3, 4)  # a = 1, b = 3, arg = (4,)
print("Result: ", res)
res = average1(1, 2, 3, 4, 5, 6, 7)  # a = 1, b = 2, arg = (2, 3, 4, 5, 6, 7)
print("Result: ", res)

# You cannot have two * parameter. Example: my_func(a, b, *args1, *args2) is not possible

# We can also use * to unpack arguments to positional arguments during function call
l = [1, 2, 3, 4]
res = average1(*l)  # unpacking l
print("Result: ", res)  # # a = 1, b = 2, arg = (2, 3)
