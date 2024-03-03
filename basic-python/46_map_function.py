# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.


def my_func(a, b, c):
    return a + b + c


list_a = [10, 20, 30, 40]
list_b = [1, 2, 3, 4]
list_c = [100, 200, 300, 400]

# Needs to provide n lists for n parameters of the functions. Equal lengths is more logical.
iterator = map(my_func, list_a, list_b, list_c)
print(type(iterator))
for result in iterator:
    print(result)
print(list(iterator))
